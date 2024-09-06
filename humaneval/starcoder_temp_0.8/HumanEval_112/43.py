
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

    # Input s,c
    # Output tuple (string, bool)
    # if true: result string is palindrome
    # else: not palindrome

    # 1. get dict from c
    d = {}
    for i in c:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # 2. use dict to remove from s
    for j in d:
        while d[j] > 0:
            s = s.replace(j, '')
            d[j] -= 1
    # 3. if empty, return palindrome
    if s == '':
        return s, True
    else:
        return s, False

