
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
    s_list = list(s)
    c_list = list(c)
    for i in range(len(s)):
        if s_list[i] == c_list[-1]:
            s_list[i] = None
            c_list.pop()
    if s_list == s_list[::-1]:
        return ''.join(x for x in s_list if x),True
    return ''.join(x for x in s_list if x),False
