
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
    result = ""
    if c in s:
        for i in range(len(s)):
            if s[i] == c:
                result = result + s[i]
            else:
                result = result + s[i] + s[i+1]
                i = i + 1
    if len(result) == 0 and len(s) > 0:
        result = s[0]
    return result, True