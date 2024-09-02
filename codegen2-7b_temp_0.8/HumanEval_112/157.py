
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
    if s == '' or c == '':
        return s,False
    
    rev_c = c[::-1]
    
    i = 0
    for char in s:
        if char == rev_c[i]:
            i+=1
            
    if i == len(c):
        return s[::-1],True
    return s,False
    
