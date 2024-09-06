
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
    # Step 1: reverse the string s
    rev_s = ''
    for i in range(len(s)-1,-1,-1):
        rev_s += s[i]
    
    # Step 2: check if string rev_s is equal to string c
    if rev_s == c:
        return (rev_s,True)
    else:
        return (rev_s,False)
