
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
    # No need to check if s or c is empty
    if s == "" or c == "":
        return "", False
    # check if s and c are palindromes
    if s == s[::-1] and c == c[::-1]:
        return s, True
    # check if c is not in s
    if c in s:
        return s.replace(c, ""), False
    # set the result string to be the reverse of s
    result = ""
    for char in s:
        result += char
    # check if the result string is palindrome
    if result == result[::-1]:
        return result, True
    else:
        return result, False
