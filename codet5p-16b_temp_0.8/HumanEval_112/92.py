
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

    dele = []
    for i in range(len(s)):
        if c.find(s[i])!= -1:
            dele.append(s[i])
    for d in dele:
        s = s.replace(d,'')
    result = (s,True) if s[::-1] == s else (s,False)
    return result
