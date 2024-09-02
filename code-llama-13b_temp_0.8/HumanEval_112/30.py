
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
    # reverse string and create a list
    s = s[::-1]
    s = list(s)

    # Go through the list to check
    for i in s:
        if i in c:
            s.remove(i)
    
    # reverse list again and return
    s = s[::-1]

    if s == s[::-1]:
        return ''.join(s), True
    else:
        return ''.join(s), False
