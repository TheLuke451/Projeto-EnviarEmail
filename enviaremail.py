

import smtplib
from email.mime.text import MIMEText

# Informações do remetente e destinatário
remetente_email = '<seu email>'
remetente_senha = '<sua senha>' # Use uma senha de aplicativo se estiver usando Gmail
destinatario_email = "<email_destino>"

# Configurações do servidor SMTP (exemplo para Gmail)
servidor_smtp = 'smtp.gmail.com'
porta_smpt = 587 # Para TLS

# Conteúdo do email
assunto = 'Email de Automação'
corpo_email = 'Este é um email enviado automaticamente como exemplo.'

# Crie o objeto de mensagem
msg = MIMEText(corpo_email)
msg['Subject'] = assunto
msg['From'] = remetente_email
msg['To'] = destinatario_email

try:
    # Conecte-se ao servidor SMTP
    server = smtplib.SMTP(servidor_smtp, porta_smpt)
    server.starttls() # Inicie o TLS para segurança
    server.login(remetente_email, remetente_senha)

    # Envie o email
    server.sendmail(remetente_email, destinatario_email, msg.as_string())

    print("Email enviado  com sucesso!")

except Exception as e:
    print(f"Erro ao enviar o email: {e}")

finally:
    #Feche a conexão com o servidor
    server.quit()