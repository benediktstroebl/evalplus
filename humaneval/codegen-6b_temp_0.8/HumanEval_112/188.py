
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
    s_rev = s[::-1]
    c_rev = c[::-1]
    for i in range(len(s)):
        if s_rev[i] == c_rev[i]:
            s_rev = s_rev[:i]+s_rev[i+1:]
    if s_rev == s:
        return s_rev, True
    return s_rev, False
