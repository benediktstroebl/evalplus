
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
    if s == "":
        return ("",True)
    
    if c == "":
        return ("",True)
    
    char_list = list(s)
    
    # reverse the string
    char_list = char_list[::-1]
    
    # delete all characters in s that are equal to any character in c
    for char in c:
        try:
            char_list.remove(char)
        except:
            continue
    
    # reverse the string again
    char_list = char_list[::-1]
    
    # return the result as a string and if it is palindrome
    if ''.join(char_list) == ''.join(char_list)[::-1]:
        return (''.join(char_list),True)
    else:
        return (''.join(char_list),False)
