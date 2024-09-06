
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
    # here, we use a list to collect all the characters in s that are not equal to any character in c
    s_list = []
    for char in s:
        if char not in c:
            s_list.append(char)
    return ''.join(s_list), ''.join(s_list)[::-1] == ''.join(s_list)

