
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
    # Check if the string is palindrome
    if s == s[::-1]:
        # Check if the string is the reverse of the other string
        if s == c[::-1]:
            return (s, True)
        # Return the result string
        return (s, False)
    else:
        # Check if the string has any character in c
        for i in range(len(s)):
            if s[i] in c:
                return (s, False)
        # Return the result string
        return (s, True)