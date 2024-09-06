
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

    # find the set of characters in string c
    c_set = set(c)
    
    # filter the string s with the set
    s_filtered = ''.join([letter for letter in s if letter not in c_set])
    
    # reverse the string
    s_reverse = s_filtered[::-1]
    
    # return a tuple
    return s_filtered, s_reverse == s_filtered
