names=['a','b','c','a','b','b','c','a','b','c']
counts=dict()

for name in names:
	counts[name]=counts.get(name,0)+1

print (counts)

for key in counts:
	print(key, counts[key])

print (counts.keys())
print (counts.values())
print (counts.items())

for k,v in counts.items():
	print (k,v)


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
	if line.startswith('From '):
		tmp=line.split()
		email=tmp[1]
		tmp=email.split('@')
		sender=tmp[0]
		print (email)
		print (sender)