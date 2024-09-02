
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

    if s == "":
        return (s,True)
    else:
        l = len(s)
        temp = s[0]
        if temp not in c:
            temp = s[1]
        else:
            c = c[1:]
        if temp not in c:
            return (temp + reverse_delete(s[1:],c),True)
        else:
            c = c[c.index(temp)+1:]
            return (temp + reverse_delete(s[1:],c),False)
