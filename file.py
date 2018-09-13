import random
import csv
dicti={} #dictionary
with open('data.csv', mode='w') as csv_file:
    fieldnames = ['character', 'frequency']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    rob=open('fileWork.txt','r') #read object
    listme=rob.readlines()
    for x in listme:
        words=x.split()
        for y in words:
            ch=random.choice(y)
            if(ch in dicti):
                dicti[ch]=dicti.get(ch)+y.count(ch)
            else:
                dicti[ch]=y.count(ch)
            print(ch,y.count(ch))
    st='a'
    flag=0
    while st<='z':
        for c in dicti:
            if(c==st):
                row=[st,dicti[c]]
                flag=1

        if(flag==0):
            row=[st,'0']
        writer.writerow({'character':st,'frequency':dicti[c]})

        chr(ord(st) + 1)
rob.close()



