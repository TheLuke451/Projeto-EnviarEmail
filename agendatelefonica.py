"""
Ensinar como manipular arquivos em python para criar uma agenda telefônica simples que guarda
nome e telefone em um arquivo agenda.txt
"""

import os
from tracemalloc import start # Importa a biblioteca 'os' para checar se o arquivo existe

ARQUIVO = "agenda.txt" # Nome do arquivo TXT que armazenará os contatos
                       # (Cada linha ="nome,telefone")

#-------------------------------
# Funções utilitárias (Apoio)
#-------------------------------

def _normaliza_texto(txt): # Função interna para remover espaços extras
    return txt.strip() # Retorna o texto sem espaços no inicio/fim


def _parse_linha(linha): # Converte uma linha "nome,telefone" em (nome, telefone)
    linha = linha.strip() # Remove quebras de linha/espacinhos 
    if not linha: # Se a linha estiver vazia
        return None # Não há contato válido
    if ',' not in linha: # Se não houver vírgula, o formato está correto
        return None # Ignora linhas inválidas
    nome, telefone = linha.split(',', 1) # Divide em duas partes 
    return _normaliza_texto(nome), _normaliza_texto(telefone) # Retorna os campos limpos

def _carrega_contatos(): # Lê todos os contatos do arquivo e devolve uma lista de tuplas (nome,telefone)
    if not os.path.exists(ARQUIVO): # Se o arquivo ainda não 
        return [] # Retorna lista vazia
    with open(ARQUIVO, 'r', encoding='utf-8') as f: # Abre o arquivo para leitura
        linhas = f.readlines() # Lê todas as linhas
    contatos = [] # Lista que armazenará os contatos válidos 
    for linha in linhas: # Percorre cada linha do arquivo
        parsed = _parse_linha(linha) # Tenta interpretar a linha do arquivo
        if parsed: # Se conseguiu interpretar
            contatos.append(parsed) # Adiciona à lista de contatos
    return contatos # Devolve a lista de contatos

def _salva_contatos(contatos): # Sobrescreve o arquivo com a lista de contatos
    with open(ARQUIVO, 'w', encoding ="utf-8") as f: # Abre o arquivo para
        for nome,telefone in contatos: # Para cada contato na linha
            f.write(f"{nome},{telefone}\n") # Escreve no formato "nome,telefone"

#----------------------------------
# CRUD: Create,Read,Update,Delete
#----------------------------------

def criar_contato(nome,telefone): #Cria (adiciona) um novo contato
    nome = _normaliza_texto(nome) # Limpa o nome
    telefone = _normaliza_texto(telefone) # Limpa o telefone
    if not nome or not telefone: # Valida campos obrigatórios
        print("Nome e telefone não podem ser vazios.") # Mensagem de erro simples
        return # Interrompe a função

    contatos = _carrega_contatos() # Carrega contatos existentes
    # Verifica duplicidade simples por nome (didático; em produção poderia checar telefone também)
    if any(c[0].lower() == nome.lower() for c in contatos): # Se já existe um contato
        print(f"Já existe um contato com o nome {nome}. Utilize atualizar_contato.")
        return # Não duplica

    # Acrescenta o novo contato e salva
    contatos.append((nome,telefone)) # Adiciona tupla (nome,telefone) à lista
    _salva_contatos(contatos) # Persiste no arquivo
    print(f"Contato {nome} adicionado com sucesso!") # Confirmação

def listar_contatos(): # Lê (exibe) todos os contatos
    contatos = _carrega_contatos() # Carrega
    if not contatos: # Se não há contatos
        print("Agenda vazia.") # Mensagem amigável
        return # Sai da função
    for i, (nome,telefone) in enumerate(contatos, start=1): # Enumera os contatos a partir de 1
        print(f"{i}. {nome} - {telefone}") # Exibe no formato "1. Nome - Telefone"

def atualizar_contato(nome_antigo, novo_nome, novo_telefone):
    nome_antigo = _normaliza_texto(nome_antigo) # Limpa nome antigo
    novo_nome = _normaliza_texto(novo_nome) # Limpa novo nome
    novo_telefone = _normaliza_texto(novo_telefone) # Limpa novo telefone
    if not novo_nome or not novo_telefone: # Valida campos
        print("Novo nome e novo telefone não podem ser vazios.") # Mensagem
        return # Sai

    contatos = _carrega_contatos() # Carrega contatos
    atualizado = False # Flag para saber se achou/ atualizou

    for idx, (nome,telefone) in enumerate(contatos): # Percorre a lista com índice
        if nome.lower() == nome_antigo.lower(): # Compara ignorando maiúsculas/minúsculas
            contatos[idx] = (novo_nome,novo_telefone) # Substitui pelo novo 
            atualizado = True # Marca que atualizou
            break # Para após a primeira ocorrência (didático)
    
    if atualizado: # Se atualizou
        _salva_contatos(contatos) # Persiste as mudanças
        print(f"Contato {nome_antigo} atualizado para {novo_nome}.") # Confirmação
    else: # Caso não encontre
        print(f"Contato {nome_antigo} não encontrado.") # Informa

def deletar_contato(nome): # Exclui um contato pelo nome
    nome = _normaliza_texto(nome) # Limpa nome
    contatos = _carrega_contatos() # Carrega contatos
    tamanho_antes = len(contatos) # Guarda Tamanho original
    #Mantém apenas os contatos cujo nome NÃO é o informado (ignora maiúsculas/minúsculas)
    contatos = [(n,t) for (n,t) in contatos if n.lower() != nome.lower()] # Filtra a lista
    if len(contatos) < tamanho_antes: # Se a lista diminuiu, alguém foi removido
        _salva_contatos(contatos) # Persiste
        print(f"Contato {nome} removido com sucesso!") # Confirma
    else: # Caso Contrário
        print(f"Contato {nome} não encontrado.") # Informa

#------------------------------
# Menu de Interação (Console)
#------------------------------

def menu(): # Função principal do menu interativo
    while True: # Loop até o usuário escolher sair
        print("\n--- Agenda Telefônica ---") # Título do menu
        print("1. Criar contato") # Opção 1
        print("2. Listar Contatos") # Opção 2
        print("3. Atualizar contato") # Opção 3
        print("4. Deletar contato") # Opção 4
        print("5. Sair") # Opção 5
        

        opcao = input("Escolha: ").strip()
        #Lê a opção do usuário e remove espaços

        if opcao =='1': # Se escolher criar
            nome = input("Nome: ")
            telefone = input("Telefone: ") # Solicita telefone
            criar_contato(nome,telefone) # Chama a função de criação
        elif opcao == '2': # Se escolhe Listar
            listar_contatos() # Lista todos
        elif opcao == '3': # Se escolher atualizar
            antigo = input("Nome do contato a atualizar: ") # Pede o nome atual
            novo = input("Novo nome: ") # Pede o novo nome
            tel = input("Novo Telefone: ") # Pede o novo telefone
            atualizar_contato(antigo,novo,tel) # Atualiza
        elif opcao == '4': # Se escolher deletar
            nome = input("Nome do contato a deletar: ") # Pede o nome a excluir
            deletar_contato(nome) # Deleta
        elif opcao == '5': # Se escolher sair
            print("Saindo...") # Mensagem de saída
            break # Interrompe o loop e encerra o programa
        else: # Qualquer outra entrada
            print("Opção inválida! Tente novamente.") # Alerta de opção inválida

# Chama o menu apenas se o arquivo for executado diretamente (boa prática)
if __name__ == '__main__': # Bloco de proteção do script
    menu() # Inicia o menu interativo