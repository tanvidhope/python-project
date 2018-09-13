import random
dicti={} #dictionary
rob=open('fileWork.txt','r') #read object
listme=rob.readlines()
wob=open('data.csv','w') #write object
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
            wob.write('%s,%s %(st,dicti[c])\n')
            flag=1

    if(flag==0):
        wob.write('%s, 0%(st)\n')
    chr(ord(st) + 1)

rob.close()
wob.close()



