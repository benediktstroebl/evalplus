
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
    #if c is None or c == '':
    #    return (s, False)
    c = set(c)
    #print(s, c)
    d = list()
    flag = False
    for x in s:
        if x in c:
            flag = True
        else:
            d.append(x)
    if flag:
        if len(d) < 2:
            return ("", False)
        else:
            if d[0] == d[-1]:
                d = d[1:-1]
                if len(d) < 2:
                    return ("", False)
                else:
                    if d[0] == d[-1]:
                        return ("".join(d[1:-1]), True)
                    else:
                        return ("".join(d), False)
            else:
                return ("".join(d), False)
    else:
        if len(s) < 2:
            return (s, False)
        else:
            if s[0] == s[-1]:
                return ("".join(s[1:-1]), True)
            else:
                return ("".join(s), False)

