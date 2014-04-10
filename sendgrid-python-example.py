import sendgrid
#import ConfigParser

#config = ConfigParser.ConfigParser()
#config.read('.env')
#
#sendgrid_username = config.get('SENDGRID', 'SENDGRID_USERNAME')
#sendgrid_password = config.get('SENDGRID', 'SENDGRID_PASSWORD')
#tos = config.get('SENDGRID', 'TOS').split(',')
#from = config.get('SENDGRID', 'FROM')

#sg = sendgrid.SendGridClient(sendgrid_username, sendgrid_password)
#message = sendgrid.Mail()
#message.add_to('John Doe <john@email.com>')
#message.set_subject('Example')
#message.set_html('Body')
#message.set_text('Body')
#message.set_from('Doe John <doe@email.com>')
#status, msg = sg.send(message)

#print sendgrid_username
#print sendgrid_password
#print tos
#print from
