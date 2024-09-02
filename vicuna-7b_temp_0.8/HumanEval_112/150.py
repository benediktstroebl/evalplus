
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
    d = len(s)
    s_temp = s[:]
    for i in range(0, d):
        if s_temp[i] == s[i]:
            s_temp.pop(i)
            c_temp = c[:]
            for j in range(0, len(c_temp)):
                if c_temp[j] == s[i]:
                    c_temp.pop(j)
    result = ''.join(s_temp)
    is_palindrome = True
    for i in range(0, len(result)):
        if result[i] != result[len(result)-i-1]:
            is_palindrome = False
    return result, is_palindrome