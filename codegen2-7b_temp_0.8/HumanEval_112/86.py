
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
    i=0
    j=0
    result = ""
    for i in range(0,len(s)):
        if s[i] in c:
            result += s[i]
    for i in range(0,len(result)):
        j = len(result)-1-i
        if result[j] == result[i]:
            result = result[:j]+result[j+1:]
    result = result[::-1]
    if result == s:
        return result, True
    return result, False
    
    
    
