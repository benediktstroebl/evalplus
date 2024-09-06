
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
    def check(s, c):
        if not s:
            return True, s
        if not c:
            return True, c
        if s[0] != c[0]:
            return True, s[:1] + c[0] + s[2:]
        for i in range(1, len(s)):
            if s[i] != c[i]:
                return True, s[:i+1] + c[0] + s[i+2:]
        return True, s[:-1] + c[1:]
    return check(s, c)[1]
