
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
    # take the letters we need to delete out of s and put them in a list
    to_remove = [l for l in s if l in c]
    # remove the letters we need to delete out of s using list comprehension
    # the slice [::-1] reverses the order of the string
    s_no_l = "".join([l for l in s if l not in c])
    # return the result of the string and a check for palindrome
    return s_no_l[::-1], s_no_l == s_no_l[::-1]
