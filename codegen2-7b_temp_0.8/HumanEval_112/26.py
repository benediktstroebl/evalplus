
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
    l1=len(s)
    l2=len(c)
    i=0
    j=0
    b=[]
    while i<l1:
        if s[i]==c[j]:
            i=i+1
            j=j+1
        else:
            i=i+1
            j=0
    if j==l2:
        return (s[:i-l2],True)
    else:
        return (s[:i-l2],False)
