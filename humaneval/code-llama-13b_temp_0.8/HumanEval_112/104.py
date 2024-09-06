
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
    #defining an empty string
    res = ''
    # go through the string s
    for ch in s:
        # if the character is not in string c then add to the result
        if ch not in c:
            res = res+ch
    # check if the res is palindrome
    if res == res[::-1]:
        return (res,True)
    else:
        return (res,False)
