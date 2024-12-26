file = open('record.txt','w')
file.write('Name: Rima \n Roll: 01 \n favourite sub: Math')
file.close()

file = open('record.txt','a')
file.write('\n Name: Naira \n Roll: 02 \n favourite sub: Math')
file.close()

file = open('record.txt','a')
file.write('\n Name:Nira \n Roll: 03 \n favourite sub: English')
file.close()

file = open('record.txt' , 'r')
print(file.read())
file.close()
