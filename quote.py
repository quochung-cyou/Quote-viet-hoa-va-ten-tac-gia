import re

a_file = open("vietnamese.txt")
b_file = open("vietnam-gen-khongdau.txt", "w")

quote = []
author = []
lines = a_file.readlines()
for line in lines:
  if "-" in line:
    quote.append(line.split('-')[0])
    author.append(line.split('-')[1])

loc = 0
for a in quote:
  b = author[loc]
  a= re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', a)
  a= re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', a)
  a= re.sub(r'[èéẹẻẽêềếệểễ]', 'e', a)
  a= re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', a)
  a= re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', a)
  a= re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', a)
  a= re.sub(r'[ìíịỉĩ]', 'i', a)
  a= re.sub(r'[ÌÍỊỈĨ]', 'I', a)
  a= re.sub(r'[ùúụủũưừứựửữ]', 'u', a)
  a= re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', a)
  a= re.sub(r'[ỳýỵỷỹ]', 'y', a)
  a= re.sub(r'[ỲÝỴỶỸ]', 'Y', a)
  a= re.sub(r'[Đ]', 'D', a)
  a= re.sub(r'[đ]', 'd', a)
  b_file.write("<quote>" + a + "\n" + "<author>" + author[loc] + "\n")
  loc = loc + 1

a_file.close()
b_file.close()