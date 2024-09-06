
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
    result = ""
    count = 0
    for i in range(len(s)):
        if s[i] in c:
            count += 1
        else:
            result += s[i]
            count = 0
    if count == 0:
        for i in range(len(result)):
            if result[i] in c:
                result = result[:i] + result[i+1:]
                count = 0
            else:
                break
    return result, count == 0
