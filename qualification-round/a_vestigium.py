testcase=int(input())
fin=testcase
output=[]
while testcase>0:
    n=int(input())
    test=[]
    b=[]
    tr_sum=0
    for i in range(n):
        row=list ( map ( int , input ( ).split()))
        test.append(row)
    
    #Trace
    for k in range(n):
        tr_sum=tr_sum+test[k][k]
    
    #row check
    row_sum=0
    for j in range(n):
        set1=set(test[j])
        if(len(set1)!=len(test[j])):
            row_sum=row_sum+1
    
    #column check    
    col_sum=0
    for l in range(n):
        a=[]
        for p in range(n):
            a.append(test[p][l])
        set2=set(a)
        if(len(set2)!=len(a)):
            col_sum=col_sum+1
        a.clear()
    b.append(tr_sum)
    b.append(row_sum)
    b.append(col_sum)
    output.append(b)
    testcase=testcase-1
for op in range(fin):
    print("Case #{}: ".format(op+1),end=" ")
    for op1 in range(len(output[op])):
        print(output[op][op1],end=" ")
    print()
    
