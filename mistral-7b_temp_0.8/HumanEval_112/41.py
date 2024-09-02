
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
    str_res = ''
    #for i in range(len(s)-1,-1,-1):
    #    if s[i] not in c:
    #        str_res = str_res+s[i]
    #return str_res,str_res==str_res[::-1]
    str_res = ''.join([x for x in s if x not in c])
    return str_res,str_res==str_res[::-1]














































































































































