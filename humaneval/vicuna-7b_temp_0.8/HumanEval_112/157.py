
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
    # Check if the input is a palindrome
    if s == reverse_string(s):
        return s, True

    # Check if the input is a palindrome
    if c == reverse_string(c):
        return s, True

    # Check if the first string is empty and the second string is not
    if len(s) == 0 and len(c) > 0:
        return c, True

    # Check if the first string is not empty and the second string is empty
    if len(c) == 0 and len(s) > 0:
        return s, True

    # Check if the first string is not empty and the second string is not empty
    # find the indices of the characters in common
    common = [i for i,c in enumerate(s) if c in c]
    i = 0
    result_string = s[:i+1] + s[common[len(common)-1]+1:]
    while i+1 < len(s) and s[i] == s[i+1]:
        i += 1
    return result_string, False
