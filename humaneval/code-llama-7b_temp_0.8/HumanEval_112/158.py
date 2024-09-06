
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    c=list(c)
    for i in range(len(c)):
        c[i]=c[i]
    l=len(c)
    d=list(s)
    n=len(s)
    if n%2==0:
        p=int(n/2)
    else:
        p=int(n/2)+1
    for i in range(0,p):
        if d[i] in c:
            d.remove(d[i])
            for j in range(i,n-i):
                d[j]=d[j+1]
            d.pop(n-1)
            n-=1
            i-=1
    if n==0:
        d=[' ']
        return (''.join(d),True)
    elif d[p:n]==d[n-1:p-1:-1]:
        return (''.join(d),True)
    else:
        return (''.join(d),False)

