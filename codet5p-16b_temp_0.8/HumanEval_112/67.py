
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

    if s == c:
        return (s,True)
    if len(s) == 0 or len(c) == 0:
        return (s,False)
    i = 0
    j = 0
    s_new = ''
    c_new = ''
    while i < len(s) and j < len(c):
        if s[i] == c[j]:
            s_new = s_new + c_new
            j += 1
        else:
            s_new = s_new + s[i]
        i += 1
    while j < len(c):
        s_new = s_new + c[j]
        j += 1
    if j!= len(c):
        s_new = s_new + c[j]
    if s_new[::-1] == s:
        return (s_new,True)
    else:
        return (s_new,False)


