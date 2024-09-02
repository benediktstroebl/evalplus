
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
    s_len = len(s)
    c_len = len(c)
    del_s = []
    i = 0
    while i < s_len:
        for j in range(c_len):
            if s[i] == c[j]:
                del_s.append(s[i])
        i += 1

    s_len -= len(del_s)
    s = s.replace(''.join(del_s),'')

    if s_len % 2 == 1:
        s_len -= 1
    for i in range(s_len//2):
        if s[i] != s[-1-i]:
            return (s,'False')
    return (s,'True')
