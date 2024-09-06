
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
    s_len = len(s)
    c_len = len(c)
    for i in range(s_len):
        for j in range(c_len):
            if s[i] == c[j]:
                del s[i]
            elif s[i:i+1] == c[j:j+1]:
                del s[i:i+1]
                break
        else:
            break
    result = s[:]
    for i in reversed(range(len(result))):
        if result[i:i+1] == c[0:len(c)//2]:
            return result,True
    return result,False