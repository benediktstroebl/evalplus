
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
    if len(s) == 0:
        return (s,True)
    if len(s) == 1:
        if s[0] != c:
            return (s,False)
        return (s,True)
    s2,c2 = s[1:],c
    if s[0] == c or s[0] == c2:
        s2 = s2[1:]
    elif s[0] != c2:
        s2 = s2.replace(s[0],'')
    return (reverse_delete(s2,c2),reverse_check(s2,c2))
