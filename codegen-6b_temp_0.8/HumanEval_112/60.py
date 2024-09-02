
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
        return (s, False)
    if not c:
        return (s, False)
    elif len(s) == 1:
        return ('', True)
    elif s[0] == c[len(c)-1]:
        temp = reverse_delete(s[1:], c[:len(c)-1])
        return (s[0] + temp[0], temp[1])
    else:
        temp = reverse_delete(s, c[:len(c)-1])
        return (temp[0] + s[0], temp[1])
