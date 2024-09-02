
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
    
    if c == "":
        return ("", True)
    
    a = s.split()
    b = c.split()
    
    if len(a) > len(b):
        a, b = b, a
        
    result = ""
    
    for s in a:
        
        for c in b:
            
            if s == c:
                result += s
                b.remove(c)
                break
    
    return (result, len(result)==
