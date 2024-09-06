
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
    s_lst = [c_i for c_i in s]
    c_lst = [c_i for c_i in c]
    for i in range(len(s_lst)):
        if s_lst[i] in c_lst:
            c_lst.remove(s_lst[i])
    if c_lst:
        return s[:-len(c_lst)],False
    else:
        return s,
