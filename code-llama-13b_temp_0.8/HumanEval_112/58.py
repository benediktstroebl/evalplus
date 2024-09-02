
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
    #reverse the string
    new_s = s[::-1]
    
    #new string with the characters that are in s and not in c
    new_str = ''
    for i in range(len(new_s)):
        if not new_s[i] in c:
            new_str += new_s[i]
            
    #return result with the result string and the result of the palindrome check
    if new_str == new_str[::-1]:
        return (new_str, True)
    else:
        return (new_str, False)
