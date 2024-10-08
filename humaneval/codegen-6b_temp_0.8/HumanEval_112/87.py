
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
    # s = [i for i in s]
    # c = [i for i in c]
    # c = set(c)
    # for i in s:
    #     if i in c:
    #         s.remove(i)
    #         c.remove(i)
    # s = "".join(s)
    # return s,s[::-1]==s
    set_c = set(c)
    for i in s:
        if i in set_c:
            s = s.replace(i,"")
            set_c.remove(i)
    return s,s[::-1] == s