
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
    # create a list of characters in c
    c = list(c)
    # remove each character from c if it is in s
    for char in c:
        if char in s:
            s = s.replace(char,"")
    # check if the result is a palindrome
    is_palindrome = True if s == s[::-1] else False
    # return a tuple containing the result string and True/False for the check.
    return (s,is_palindrome)
