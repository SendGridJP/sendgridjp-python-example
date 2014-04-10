from smtpapi import SMTPAPIHeader

header = SMTPAPIHeader()

#header.set_substitutions({'fullname': ['田中 太郎', '佐藤 次郎', '鈴木 三郎'], "familyname": ["田中", "佐藤", "鈴木"], "place": ["office", "home", "office"]})
header.add_substitution('fullname', ['田中 太郎', '佐藤 次郎', '鈴木 三郎'])
header.add_substitution("familyname", ["田中", "佐藤", "鈴木"])
header.add_substitution("place", ["office", "home", "office"])
header.add_section('office', '中野')
header.add_section('home', '目黒')
header.add_category('カテゴリ1')

print(header.json_string())
