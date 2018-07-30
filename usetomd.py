import tomd

f = open('in.txt', mode='r', encoding='UTF-8')
contents = f.read()

f_out = open('out.md', 'w+', encoding='UTF-8')
soup = tomd.convert(contents)
f_out.write(soup)

f.close()
f_out.close()
