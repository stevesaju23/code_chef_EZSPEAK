n=int(input())
for i in range(0,n):
    l=int(input())
    s=input()
    con=0
    for i in range(l-1):
        if con==3:
            break
        elif s[i] not in ["a","e","i","o","u"] and s[i+1] not in ["a","e","i","o","u"]:
            con+=1
        else:
            con=0
    if con==3:
        print("NO")
    else:
        print("YES")
