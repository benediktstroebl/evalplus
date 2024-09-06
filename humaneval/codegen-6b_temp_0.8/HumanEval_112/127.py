
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
    # replace letters in s
    # delete from s letters that are equal to any value in c
    # if s is still a palindrome, return (s,True)
    # else return (s,False)
    s = s.replace(c, '')
    s = s.replace(c.lower(), '')
    s = s.replace(c.upper(), '')
    return s, s == s[::-1]
