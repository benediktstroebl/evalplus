
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
    # If s contains any character in c then return a tuple (reversed s, False)
    if set(s).intersection(set(c)):
        return s[::-1], False
    # If s is empty and c is not empty, then return ('', True)
    elif len(s) == 0 and len(c) > 0:
        return '', True
    # If s is not empty and c is empty, then return (s, True)
    else:
        return s, True
