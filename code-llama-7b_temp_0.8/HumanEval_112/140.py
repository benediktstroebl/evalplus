
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
    # Reverse the s and compare with itself.
    # If the result is the same as the original s, the result is a palindrome.
    if c == s[::-1]:
        return s, True

    for i in range(len(s)):
        s = s[:i] + s[i+1:]
        if c == s[::-1]:
            return s, True
        s = s[:i] + s[i] + s[i+1:]

    return s, False
