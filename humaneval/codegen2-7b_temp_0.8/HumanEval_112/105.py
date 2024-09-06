
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
    a=0
    b=len(s)-1
    while a<len(s) and b>=0:
        if s[a]==c[0]:
            for i in range(len(c)):
                if s[b]==c[i]:
                    b=b-1
                    a=a+1
                    break
        a=a+1
        b=b-1
    if b==-1:
        return (s,True)
    return (s,False
