
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
    s_len = len(s)
    c_len = len(c)
    result = s[:s_len] + s[s_len-c_len:]
    for i in range(s_len):
        if s[i] in c:
            result = result[0:(i+1)] + result[i+1:]
    if result == s[::-1]:
        return result,True
    else:
        return result,False
