
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
    if s == "" and c == "":
        return (s, True)
    elif s == "":
        return ("".join(c), False)
    elif c == "":
        return ("".join(s), False)
    elif s[-1]!= c[0]:
        return ("".join(s), False)
    elif s[0]!= c[0]:
        return ("".join(s), False)
    else:
        return ("".join(s[0:-1]), s[0:-1] == s[1:])

