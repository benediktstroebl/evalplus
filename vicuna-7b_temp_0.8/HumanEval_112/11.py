
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
    if len(s) == 0 or len(c) == 0:
        return '', False
    i,j = 0,len(s)-1
    while i<=j:
        if s[i] == c[j]:
            del s[i],s[j]
            i,j = i+1,j-1
        else:
            i,j = i+1,j
    return s, True if s == reverse_string(s) else False
