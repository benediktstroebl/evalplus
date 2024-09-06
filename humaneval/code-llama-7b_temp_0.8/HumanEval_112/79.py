
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
    s = s[::-1]
    c = c[::-1]
    for i in range(len(s)-len(c)+1):
        for j in range(len(c)):
            if s[i+j]==c[j]:
                s = s[:i]+s[i+j+1:]
                break
    return s, s[::-1]==s

