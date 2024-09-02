
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
    for ch in c_list:
        i = 0
        while i < len(s_list):
            if s_list[i] == ch:
                s_list.pop(i)
            else:
                i += 1
    return ("".join(s_list), False) if s_list == list(s) else ("".join(s_list), True)

