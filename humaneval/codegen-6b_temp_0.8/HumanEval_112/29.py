
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
    s = s.lower()
    c = c.lower()

    char_list = []
    l_s = len(s)
    l_c = len(c)
    for i in range(0,l_s-l_c+1):
        char = s[i:i+l_c]
        if char in c:
            char_list.append(char)
    char_list.sort(reverse=True)
    l_list = len(char_list)
    del_s = ''
    for i in range(0,l_list):
        del_s = del_s + char_list[i]
    if del_s == del_s[::-1]:
        return (del_s, True)
    else:
        return (del_s, False)
