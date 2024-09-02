
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
    
    #create a copy of the string, as we are going to change the string
    s_new = s
    
    #for each character in c we are going to check if it exists in s
    #if it exists we are going to delete it from the copy string
    for char in c:
        s_new = s_new.replace(char,'')
    
    #we are going to check if the new string is palindrome
    if s_new[::-1] == s_new:
        return s_new, True
    else:
        return s_new, False
