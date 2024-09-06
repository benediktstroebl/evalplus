
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
    c = list(c)
    s = list(s)
    i = 0
    j = len(s)-1
    s_c = []
    while i < len(s):
        if c[j] == s[i]:
            s[i] = ""
            j -= 1
            i += 1
            continue
        else:
            s_c.append(c[j])
            j -= 1
    s_c = ''.join(s_c)
    if s_c == s:
        return (s_c, True)
    else:
        return (s_c, False)
