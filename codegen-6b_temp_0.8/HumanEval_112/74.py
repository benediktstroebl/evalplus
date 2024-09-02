
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
    # your code here
    # return (s,True) if s == s[::-1] else (s[::-1],False)
    return (s.replace(c, ''), s == s[::-1])

assert reverse_delete('abcde', 'ae') == ('bcd', False)
assert reverse_delete('abcdef', 'b') == ('acdef', False)
assert reverse_delete('abcdedcba', 'ab') == ('cdedc', True)
assert reverse_delete('abcdedcba', 'a') == ('abcdedcba', True)
assert reverse_delete('abcdedcba', 'ab') == ('cdedcba', True)
assert reverse_delete('abcdedcba', 'x') == ('abcdedcba', True)
