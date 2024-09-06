
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
    # for i in c:
    #     s = s.replace(i,'')
    # return s, s[::-1] == s
    
    # caution: use replace method before reversing the string, otherwise it will mess up the
    # first letter of the string
    # return (s, s[::-1].replace(''.join(c), '') == s)
    
    # or you can replace all the characters by an empty string
    # return (s, s[::-1].replace(c,'') == s)

    # or you can delete the characters directly
    for i in c:
        s = s.replace(i,'')
    return s, s[::-1] == s
