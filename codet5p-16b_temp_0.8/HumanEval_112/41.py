
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

    s = s.replace(" ", "")
    c = c.replace(" ", "")
    result = s[:]
    for s_char in s:
        if s_char in c:
            result = result.replace(s_char,"")
    result = result.replace(" ", "")
    result = result[::-1]
    if result == s:
        return (result, True)
    else:
        return (result, False)

