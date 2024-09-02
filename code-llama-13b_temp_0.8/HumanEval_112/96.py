
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
    c = set(c) # Converting to set for O(1) lookup
    s = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        while start < end and s[start] in c: # Left Pointer
            start += 1
        while start < end and s[end] in c: # Right Pointer
            end -= 1
        if start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    if start == end:
        if s[start] in c:
            return '', False
        else:
            return ''.join(s), True
    return ''.join(s[:start]), True if not s[end:] else False

