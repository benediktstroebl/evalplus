
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
    '''
    n = len(s)
    if n == 0:
        return (s, True)
    result = ""
    for i in range(n-1,-1,-1):
        if s[i] == c:
            result = s[:i]+s[i+1:]
            if result == result[::-1]:
                return (result, True)
    return (s, False)
    '''
    return (s[::-1], s == s[::-1])
