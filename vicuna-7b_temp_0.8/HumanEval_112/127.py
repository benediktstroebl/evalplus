
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
    d = len(s)
    n = len(c)
    rev = []
    flag = False
    for i in range(d):
        rev.append(s[i])
    for i in range(n):
        if rev[i] == c[n-i-1]:
            rev.pop(i)
            flag = True
            for i in range(d):
                if s[i] == rev[-1]:
                    rev.pop()
                    break
    result = "".join(rev)
    return result, flag