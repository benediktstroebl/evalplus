
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
    # the way I did it is kinda lengthy, I'm sure there is a better way to do it
    # I am not entirely sure how the reverse_delete function is supposed to work
    # I just did it without the palindrome part, we could easily add that later
    l = []
    for x in s:
        if x not in c:
            l.append(x)
    return ''.join(l), s == ''.join(reversed(l))
