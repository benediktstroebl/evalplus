
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

    if len(s) == 1:
        if s[0] == c[0]:
            return (s,True)
        else:
            return (s,False)
    else:
        index = 0
        while s[index] == c[0]:
            index += 1
        if index == len(s):
            return (s,False)
        else:
            s_sub = s[:index] + s[index+1:]
            return (reverse_delete(s_sub,c),True)
