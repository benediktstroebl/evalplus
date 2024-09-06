
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
    found = {}
    for c in c:
        if c in s:
            found[c] = found.get(c, 0) + 1
    result = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] in found:
            found[s[i]] -= 1
            if found[s[i]] == 0:
                del found[s[i]]
        result += s[i]
    return (result, result==s)
