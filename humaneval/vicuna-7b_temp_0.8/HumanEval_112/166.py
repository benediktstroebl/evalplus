
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
    if not s:
        return s, False
    if not c:
        return s, False
    if c in s:
        s = s.replace(c, '')
        s = s.join('')
        return s, True
    else:
        s, flag = reverse_delete(s, c)
        if flag:
            return s, True
        else:
            return s, False
