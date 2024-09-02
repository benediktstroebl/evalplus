
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
    result = ""
    d = {}
    for c in c:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] in d:
                d[s[i:j]] -= 1
            else:
                d[s[i:j]] = -1
        if d[s[i:j]] == 0:
            del d[s[i:j]]
        result += s[i:j]
    return result, True
