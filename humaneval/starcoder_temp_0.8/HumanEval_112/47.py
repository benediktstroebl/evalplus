
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

    n = len(s)
    s = s.lower()
    c = c.lower()
    s_ = ""
    s_reverse = ""
    for i in range(n):
        if s[i] not in c:
            s_ += s[i]
    if s_ == s_[::-1]:
        return (s_,True)
    else:
        for i in range(n):
            if s[i] in c:
                s_reverse += s[i]
        if s_reverse == s_reverse[::-1]:
            return (s_reverse,True)
        else:
            return (s_,False)
