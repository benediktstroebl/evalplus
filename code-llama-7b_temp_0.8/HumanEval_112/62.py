
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

    # putting everything in a list and removing all the chars in the list
    l = []
    for char in s:
        if char not in c:
            l.append(char)
    s = "".join(l)

    # return s and True if s is a palindrome or False if it's not
    # check here if the string is a palindrome using recursion
    return check_palindrome(s)

