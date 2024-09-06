
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
    # your code here
    s_len = len(s)
    c_len = len(c)
    s_new = ""
    i = j = 0
    while i < s_len:
        if s[i] != c[j]:
            s_new += s[i]
            i += 1
        else:
            j += 1
            if j > c_len:
                break
    # check if the result string is palindrome
    if s_new == s[::-1]:
        return (s_new, True)
    else:
        return (s_new, False)

result = reverse_delete(s,c)
