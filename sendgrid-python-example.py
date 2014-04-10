import sendgrid
import configparser

config = configparser.ConfigParser()
config.read('.env')

sendgrid_username = config.get('SENDGRID', 'SENDGRID_USERNAME')
sendgrid_password = config.get('SENDGRID', 'SENDGRID_PASSWORD')
tos = config.get('SENDGRID', 'TOS').split(',')
from_address = config.get('SENDGRID', 'FROM')

sg = sendgrid.SendGridClient(sendgrid_username, sendgrid_password)
message = sendgrid.Mail()
message.add_to(tos)
message.set_from('送信者名 <' + from_address + '>')
message.set_subject('[sendgrid-python-example] フクロウのお名前はfullnameさん')
message.set_text('familyname さんは何をしていますか？\r\n 彼はplaceにいます。')
message.set_html('<strong> familyname さんは何をしていますか？</strong><br />彼はplaceにいます。')
message.set_substitutions({'fullname': ['田中 太郎', '佐藤 次郎', '鈴木 三郎'], "familyname": ["田中", "佐藤", "鈴木"], "place": ["office", "home", "office"]})
#message.add_substitution("familyname", ["田中", "佐藤", "鈴木"])
#message.add_substitution("place", ["office", "home", "office"])
message.add_section('office', '中野')
message.add_section('home', '目黒')
message.add_category('カテゴリ1')

status, msg = sg.send(message)

print(status)
print(msg)
