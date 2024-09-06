
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
    # convert characters in c to lowercase
    c = [x.lower() for x in c]

    # remove all characters from s that are in c
    s = [x for x in s if x not in c]

    # reverse the characters in s
    s = s[::-1]

    # check if s is a palindrome
    if s == s[::-1]:
        return s, True
    else:
        return s, False
