
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
    s = s[::-1]
    c = c[::-1]
    new = ""
    for i in s:
        if i in c:
            pass
        else:
            new += i
    return new, new[::-1] == new
    #return s[::-1]
        
    # result = ""
    # for i in range(len(s)-1,-1,-1):
    #     if s[i] in c:
    #         pass
    #     else:
    #         result += s[i]
    # return result[::-1]
    # if s == '':
    #     return s
    # elif s[0] in c:
    #     return reverse_delete(s[1:],c)
    # else:
    #     return reverse_delete(s[1:],c) + s[0]
    
    # result = ""
    # for i in range(len(s)-1,-1,-1):
    #     if s[i] in c:
    #         pass
    #     else:
    #         result += s[i]
    # return result[::-1]
    # return s[::-1]
    # if s == '':
    #     return s
    # else:
    #     return reverse_delete(s[1:],c) + s[0]
    # if s == '':
    #     return s
    # if s[0] in c:
    #     return reverse_delete(s[1:],c)
    # else:
    #     return reverse_delete(s[1:],c) + s[0]
    # if s == '':
    #     return s
    # if s[0] in c:
    #     return reverse_delete(s[1:],c)
    # else:
    #     return reverse_delete(s[1:],c) + s[0]
    # if s == '':
    #     return s
    # if s[0] in c:
    #     return reverse_delete(s[1:],c)
    # else:
    #    
