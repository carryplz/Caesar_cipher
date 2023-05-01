import string


pri = input("input: ")
pri = pri.upper()
tt = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[3:] + string.ascii_uppercase[:3])

prese = pri.translate(tt)

print(prese)

