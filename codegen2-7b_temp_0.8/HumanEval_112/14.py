
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
    string_length=len(s)
    if string_length==0:
        return "",True
    if string_length==1:
        if s[0]==c[0]:
            return s,True
        return s,False
    for i in range(len(s)-1):
        if s[i]==c[0]:
            s=s[:i]+s[i+1:]
    for i in range(len(s)-1):
        if s[i]==c[-1]:
            s=s[:i]+s[i+1:]
    return s,
