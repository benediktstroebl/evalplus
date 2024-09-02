
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

    if len(s)<len(c):
        return s,False
    #Step 1: Checking Palindrome
    x = s[::-1]
    y = s

    if x==y:
        return s,False
    
    #Step 2: Removing letters from s
    x = set(c)

    for i in x:
        s = s.replace(i,"")
    
    return s,True
