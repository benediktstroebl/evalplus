
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
    def check_palindrome(str):
        return str[::-1] == str
    i = 0
    while i < len(s):
        if s[i] in c:
            s = s[:i] + s[i+1:]
            if len(s) == 0:
                return ("",True)
            i = 0
        else:
            i += 1
    return (s,check_palindrome(s))

