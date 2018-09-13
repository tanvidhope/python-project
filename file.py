import random
import csv
import re
dicti={} #dictionary
with open('data.csv', mode='w') as csv_file:
    fieldnames = ['character', 'frequency']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    rob=open('fileWork.txt','r') #read object
    listme=rob.readlines()
    for x in listme:
        words = re.findall(r"[\w]+|[^\s\w]",x)
        for y in words:
            ch=random.choice(y)
            if(ch in dicti):
                dicti[ch]=dicti.get(ch)+y.count(ch)
            else:
                dicti[ch]=y.count(ch)
    #print (dicti)
    st='a'
    while st<='z':
        flag=0
        for c in dicti:
            if(c==st):
                writer.writerow({'character':st,'frequency':dicti[c]})
                flag=1
        if(flag==0):
            writer.writerow({'character':st,'frequency':'0'})
        st=chr(ord(st) + 1)
rob.close()




