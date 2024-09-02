
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
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j] and s[i] != c:
            s = s[0:i] + s[i+1:j] + s[i] + s[j+1:]
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1
    return s,s == s[::-1]
