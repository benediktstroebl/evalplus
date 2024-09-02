
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
    s_list_clean = []
    for c_new in c:
        if c_new not in s_list_clean:
            s_list_clean.append(c_new)
        else:
            continue
    
    for c_old in s_list:
        if c_old in s_list_clean:
            s_list.remove(c_old)
    
    if s_list == s_list[::-1]:
        return ("".join(s_list),True)
    else:
        return ("".join(s_list),False)
