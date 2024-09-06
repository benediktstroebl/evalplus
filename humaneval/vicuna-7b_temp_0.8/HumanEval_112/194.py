
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
    if len(s) == 0:
        return '',False
    if len(c) == 0:
        return '',False
    result = []
    count = 0
    for i in range(len(s)):
        if s[i] == c[count]:
            count += 1
        else:
            result.append(s[i])
            count = 0
    result.append(s[len(s)-1])
    if s[len(s)-1] == c[0]:
        return ''.join(reversed(result)),True
    else:
        return ''.join(reversed(result)),False
