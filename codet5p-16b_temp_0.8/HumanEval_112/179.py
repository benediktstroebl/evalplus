
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

    start = 0
    end = len(s) - 1
    new_s = []
    while start < end:
        if s[start]!= c[0]:
            new_s.append(s[start])
        elif s[start] == c[0]:
            while start < end and s[start] == c[0]:
                new_s.append(s[start])
                start += 1
        start += 1
        if start == end:
            new_s.append(s[end])
        if s[end]!= c[0]:
            new_s.append(s[end])
        elif s[end] == c[0]:
            while start < end and s[end] == c[0]:
                new_s.append(s[end])
                end -= 1
        end -= 1
    return (''.join(new_s), False)












