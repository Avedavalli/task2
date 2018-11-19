l1=[i for i in input("entr list 1 values , seprated").split(',')]
l2=[i for i in input("entr list 2 values , seprated").split(',')]
'''for i in l1:
    for j in l2:
        if i==j:
            print(i,'is common') or'''
c=[];nc=[]
for i in l1:
    if i in l2:
        c.append(i)
    else:
        nc.append(i)
print(c,"are the common ones and ",nc,"are not")
    
    
            
