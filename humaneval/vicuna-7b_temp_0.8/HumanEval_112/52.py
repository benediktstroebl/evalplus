
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
    count = 0
    for c1 in s:
        if c1 not in c:
            result += c1
        count += 1
    if count == 0:
        return s, True
    for count2 in range(0, len(s)):
        if s[count2] == s[len(s) - count2 - 1]:
            count += 1
            if count == len(s):
                return result, True
            result += s[count2]
    return result, False
