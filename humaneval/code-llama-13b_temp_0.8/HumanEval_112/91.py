
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
    # Get char index in string
    indexes = [i for i,x in enumerate(s) if x in c]
    # Reverse string
    s = s[::-1]
    # Get char index in reversed string
    indexes_r = [i for i,x in enumerate(s) if x in c]
    # Reverse char index
    indexes_r.reverse()
    # Sum them together
    indexes += indexes_r
    # Remove all indexes in reversed string
    return s[:indexes[0]], s[indexes[0]:] == s[indexes[0]:][::-1]
