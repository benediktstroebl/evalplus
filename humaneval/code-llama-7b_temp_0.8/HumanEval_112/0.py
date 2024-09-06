
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
    # return the string with all instances of c removed
    # i = s.find(c)
    # while i >= 0:
    #     s = s[:i] + s[i+1:]
    #     i = s.find(c, i+1)
    # return s
    # r = s
    # for i in c:
    #     r = r.replace(i, "")
    # return r
    for i in c:
        s = s.replace(i, "")
    return s

