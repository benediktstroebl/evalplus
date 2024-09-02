
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
    c_dict = dict.fromkeys(c, 0)
    for c in s:
        if c in c_dict:
            c_dict[c] += 1
    c_dict = {k: v for k, v in c_dict.items() if v > 0}
    for c in c_dict:
        s = s.replace(c, "")
    if s == s[::-1]:
        return (s, True)
    return (s, False)
