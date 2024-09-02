
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
    i = 0
    j = len(s)-1
    new_str = ""
    while i <= j:
        if s[i] == c:
            new_str += ""
            i += 1
        elif s[j] == c:
            j -= 1
            new_str += ""
        else:
            new_str += s[i]
            i += 1
            new_str += s[j]
            j -= 1
    return new_str  
