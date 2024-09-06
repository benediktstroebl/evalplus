
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
    for i in range(len(s)):
        if s[i] in c:
            del s_list[i]
            s = ''.join(s_list)
    s = ''.join(s_list)
    # Check if the result string is palindrome
    s_length = len(s)
    for i in range(s_length // 2):
        if s[i] != s[s_length - i - 1]:
            return s, False
    return s, True


