##Selecionando alinhamentos de BLAST all-vs-all de diferentes tratamentos

arq1 = open('BLAST_ctgs_nr_corrigido.txt', 'r') #Arquivo BLAST contendo os alinhamentos
arq = open('alings_nr_cover-2.txt', 'w') #Arquivo a ser criado segundo o parâmetro escolhido
l = []
red = []

for line in arq1:
  line = line.strip('\t')
  l.append(line)
  
#print(l)

for line in l:
  z = line
  line = line.replace('\t', ' ')
  line = line.split(' ')
  line = line[:4]
  if line[1] == 'Query:':
    lenght = line[3]
    lenght = (int(lenght[4:]))-2 # tamanho do contig. mutiplicamos pelo valor que qremos de cobertura
    #print(lenght)
  
  a = line[0]
  b = line[1]
  #print(line)
  if a[0] == '*' and b[0] == '*':
    cover = int(line[3])
    rg = float(line[2])
    #print(cover, rg)
    if a != b:
      if cover >= lenght and rg >= 98.5: #Nesse ponto é feita a seleção dos alinhamentos seguindo esses parâmetros 
        #print(rg, cover)
        #print('^^^^')
        arq.write(z)
        red.append(a) # A REPRESENTA OS QUERYS E QNTAS VEZES ELES ALINHAM 
  
print(red)
print(len(red))
t = []
for item in red:
  [ t.append(item) for item in red if not t.count(item) ]

arq2 = open('ctgsreduntes_nr_cover-2.txt', 'w') #nesse arquivo estarão todos contigs query, indepente de ter alinhado 1x ou mais vezes
for line in t:
  arq2.write(line)
  arq2.write('\n')

arq2.close()
print(t)
print(len(t)) #controle:
arq.close()