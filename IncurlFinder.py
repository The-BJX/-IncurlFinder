def filt(str):
    res=""
    for i in str:
        if '0'<=i and i<='9':
            continue
        res=res+i
    return res
#输入
#当接收到换行和 fin 时
句读=['？','！','。','，','：','；','”','“','（','）']

文章=''
句=input()
while 句!='fin':
    文章=文章+'。'+句
    句=input()
文章=filt(文章)

#丢尽map里面
字典={'begin_output':[]}
for i in range(0,len(文章)):
    if not(字典.get(文章[i])):
        字典[文章[i]]=[]
    字典[文章[i]].append(i)
#print(字典)


for i in 字典.keys():
    #遍历每一个字
    if i in 句读: 
        continue
    if '0'<=i and i<='9':
        continue
    if len(字典[i])==1:
        continue
    print(i)
    for j in 字典[i]:
        #遍历每一次出现的地方
        l=j
        r=j
        while not(文章[l] in 句读 or l==0):
            l-=1
        if 文章[l] in 句读:
            l+=1
        while not(文章[r] in 句读 or r==len(文章)-1):
            r+=1
        if 文章[r] in 句读:
            r-=1

        print(文章[l:r+1])
    print (" ")
