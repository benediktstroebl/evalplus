
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
    # Fixed length, and all characters are present
    # O(n) time, O(1) space
    # for c_ in c:
    #     s = s.replace(c_, '')
    # return (s, s[::-1] == s)

    # Dynamic length, not all characters are present
    # O(n * m) time, O(1) space
    for c_ in c:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == c_:
                s = s[:i] + s[i + 1:]
                j -= 1
            elif s[j] == c_:
                s = s[:j] + s[j + 1:]
                j -= 1
            else:
                i += 1
                j -= 1
    return (s, s[::-1] == s)

