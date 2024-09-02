
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
    i, j = 0, len(s)-1
    while i < j:
        while i < j and s[i] in c:
            i += 1
        while i < j and s[j] in c:
            j -= 1
        if s[i] == s[j]:
            i += 1
            j -= 1
    return (s[:i]+s[j+1:], s[i:j+1] == s[i:j+1][::-1])
