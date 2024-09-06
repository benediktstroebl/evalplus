
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
    def is_palin(s, c = None):
        if c is None:
            if not s:
                return True
            return s[0] == s[-1] and is_palin(s[1:-1])
        if not s or not c:
            return (True if not s or not c else False)
        return s[0] == c and is_palin(s[1:]) and is_palin(s[:-1])

    def replace(s, c):
        if not s:
            return s
        return c + replace(s[1:], c) if s[0] == c else s

    return ((c + replace(s[::-1], c)) if is_palin(s) else s, is_palin(s, c))

