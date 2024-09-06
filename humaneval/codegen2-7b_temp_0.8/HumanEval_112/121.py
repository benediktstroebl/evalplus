
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
    n1 = 0
    n2 = 0
    i = 0
    j = 0
    for i in range(len(s)):
        for j in range(len(c)):
            if s[i] == c[j]:
                n1 = i
                n2 = j
    if n2 == (len(c) - 1):
        return (s[:n1],True)
    else:
        return (s[:n1] + s[n2 + 1:],
