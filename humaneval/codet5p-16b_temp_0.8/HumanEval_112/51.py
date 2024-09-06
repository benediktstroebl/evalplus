
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

    if s == None or c == None:
        return None
    index = 0
    res = ''
    while index < len(s):
        if s[index] not in c:
            res += s[index]
            index += 1
        else:
            s = s[:index] + s[index+1:]
            index = 0
    return (res,res == res[::-1])
