
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
    a=[]
    b=[]
    c=[]
    d=[]
    s=[]
    for i in range(len(s)):
        if s[i] not in c:
            a.append(s[i])
        elif s[i] in c:
            b.append(s[i])
    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if b[j]==b[len(b)-1-j]:
                c.append(b[j])
            else:
                d.append(b[j])
        b.remove(b[len(b)-1])
    s.append(''.join(c))
    s.append(''.join(a))
    s.append(''.join(d))
    return s
