
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
    s_set = set(s)
    c_set = set(c)
    s_len = len(s)
    c_len = len(c)
    for i in range(s_len):
        if c_set.intersection(set(s[i:i+1])) != set():
            s_set.remove(s[i])
    result_str = ''.join(s_set)
    return result_str, True
