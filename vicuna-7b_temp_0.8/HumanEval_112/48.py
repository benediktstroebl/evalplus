
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
    rev_s = [s[i:j] for i,j in zip([0]+list(range(len(s))), [0]+list(range(len(s))))]
    result = ''
    for i in range(len(rev_s)):
        if rev_s[i] == rev_c[i]:
            del rev_s[i]
        else:
            result += rev_s[i]
    return (result, True) if s == reverse_join(list(map(str, rev_s))) else (result, False)
