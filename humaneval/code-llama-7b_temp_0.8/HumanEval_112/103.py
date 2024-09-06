
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
    # s = str(s)
    # c = str(c)
    #
    # x = []
    # y = []
    # z = []
    # for i in c:
    #     x.append(i)
    # for j in s:
    #     y.append(j)
    # for k in y:
    #     if k in x:
    #         z.append(k)
    # x = ''.join(z)
    # return x
    s = str(s)
    c = str(c)
    x = []
    y = []
    for i in s:
        if i not in c:
            x.append(i)
    for i in c:
        if i not in s:
            y.append(i)
    print(y)
    print(x)
    z = "".join(x)
    print(z)
    if z == z[::-1]:
        return True
    else:
        return False
