filename = raw_input('Filename?') #Acquire file
f = open(filename,'r')
raw = f.read()
f.close()
fin = ''
for char in list(raw): #for every character in code, append sooubwayheck equivalent.
 if char == '>':
  fin += 'soubway\n'
 elif char == '<':
  fin += 'sooubway\n'
 elif char == '+':
  fin += 'soooubway\n'
 elif char == '-':
  fin += 'sooooubway\n'
 elif char == '.':
  fin += 'soooooubway\n'
 elif char == ',':
  fin += 'sooooooubway\n'
 elif char == '[':
  fin += 'soooooooubway\n'
 elif char == ']':
  fin += 'sooooooooubway\n'
f = open(filename + '.sub','w') #write file with .sub extension
f.write(fin)
f.close()
