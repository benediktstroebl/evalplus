
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
    rev_c = sorted(set(c))
    rev_s = [s[i:i+1] for i in range(len(s)-1)]
    for i in range(len(rev_s)):
        if any(c in x for x in rev_s[i+1:]):
            rev_s[i] = ' '
            rev_s = rev_s[:i+1]+rev_s[i+2:]
    result = ''.join(rev_s)
    return result, True