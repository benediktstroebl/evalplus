
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
    # Version 1
    # result = s
    # for i in c:
    #     result = result.replace(i,'')
    # if result == result[::-1]:
    #     return (result,True)
    # return (result,False)

    # Version 2
    # return (s[:len(s)-len(s.translate(str.maketrans(c,c)))],s[:len(s)-len(s.translate(str.maketrans(c,c)))].translate(str.maketrans(c,c)) == s[:len(s)-len(s.translate(str.maketrans(c,c)))].translate(str.maketrans(c,c))[::-1])

    # Version 3
    # return (s.translate(str.maketrans(c,c)),s.translate(str.maketrans(c,c)) == s.translate(str.maketrans(c,c))[::-1])

    # Version 4
    return (s.translate(str.maketrans(c,c)),s.translate(str.maketrans(c,c)) == s[::-1])

