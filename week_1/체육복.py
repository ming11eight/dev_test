# 탐욕법 - 체육복
def solution(n, lost, reserve):
    #방법1
    '''
    u=[1]*(n+2)
    for i in reserve:
        u[i]+=1
    for i in lost:
        u[i]-=1
    for i in range(1,n+1):
        if u[i-1]==0 and u[i]==2:
            u[i-1:i+1]=[1,1]
        elif u[i]==2 and u[i+1]==0:
            u[i:i+2]=[1,1]
    return len([x for x in u[1:n+1] if x>0])
    '''
    
    #방법2
    s = set(lost) & set(reserve)
    r = set(reserve)-s
    l = set(lost)-s
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    return n-len(l)