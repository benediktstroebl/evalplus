
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
    s_copy = s.lower()
    c_copy = c.lower()
    result = ""
    count = 0
    for i in range(len(s_copy)):
        if s_copy[i] not in c_copy:
            result += s_copy[i]
        else:
            count += 1
            if count > 1:
                result += s_copy[i]
    return (result, count > 1)
