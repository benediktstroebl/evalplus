
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
    # get length of s
    n = len(s)
    # create a variable to store the count of characters in s
    count = 0
    # iterate through all the characters in s
    for i in range(n):
        count += s[i] == s[i+1]
    # for the characters in c
    for j in range(len(c)):
        count -= s[j] == c[j]
    # return the result string and True/False for the check
    return (s[:count],count!=len(s))