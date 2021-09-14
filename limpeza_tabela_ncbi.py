##Limpeza tabela do BLAST do NCBI

arq1 = open('gg.txt', 'r') #arquivo contendo o output do NCBI
l = []
m = []
n = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = [] #foram criadas varias listas apenas para conferir oq estava sendo encaminhado a cada uma delas para saber se alguma informação seria perdida
for line in arq1:
  if line[0] == 'Q' and line[6] != '#':
    m.append(line)
  elif line[0] == 'S' and line[1] == 'b':
    n.append(line)
  elif line[0] == ' ': #retira todas as ||||||
    c.append(line)
  else:
    if line == '\n':
      d.append(line)
    elif line[0] == '>':
      e.append(line)
    elif line[0] =='R' and line[1] == 'a' and line[2] == 'n' and line[4] == 'e':
      g.append(line)
    elif line[0] == 'S' and line[9] == 'I':
      f.append(line)
    elif line[0] == 'S' and line[4] == 'e':
      h.append(line)
    elif line[0] == 'A' and line[5] == 'm' and line[9] == 's':
      i.append(line)
    elif line[0] == 'I' and line[3] == 'n' and line[6] =='t' and line[9] == 's':
      j.append(line)
        
    else:
      if line[0] == 'Q' and line[4] == 'y':
        line = '\n' + line
        
      l.append(line)
print(l)
arq2 = open('BLAST_Sc_ctgsgrandes_X_nr7.txt', 'w') #arquivo a ser gerado contendo as informações filtradas 
for line in l:
  arq2.write(line)
arq1.close()
arq2.close()
