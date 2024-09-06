
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
    # should return (string, bool)
    filtered = [letter for letter in s if letter not in c]
    filtered = ''.join(filtered)
    # if string is empty and length of filtered string is 0
    if len(filtered) == 0 and len(s) > 0:
        return (s, False)
    # if filtered string is empty and length of string is not 0
    elif len(s) > 0 and len(filtered) == 0:
        return (filtered, False)
    else:
        return (filtered, filtered == filtered[::-1])
