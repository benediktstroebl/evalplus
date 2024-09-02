
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
    a=s
    b=c
    c=len(b)
    d=[]
    for i in range(c):
        d.append(a[0])
        a=a[1:len(a)]
    s=d[::-1]
    e=list(s)
    #print(e)
    i=0
    for i in range(len(s)):
        if e[i] in b:
            e[i]=' '
        #print(e[i])
    #print(e)
    a=''.join(e)
    #print(a)
    b=a[::-1]
    if a==b:
        return (a,True)
    else:
        return (a,False)



