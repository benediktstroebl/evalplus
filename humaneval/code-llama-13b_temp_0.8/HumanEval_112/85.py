
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
    # Algo 
    # iterate through s until a character in c is encountered.
    # when a character in c is encountered, 
    # iterate backwards from that character in c till the end of the string.
    # check if the characters are the same for both.
    # if so, continue from that character in c till the end of the string
    
    # reverse the string and check if it's the same as the original string
    
    # return the result string and True/False for the check
    # clarification:
    # when a character in c is encountered, iterate backwards from that character in c till the end of the string. 
    # check if the characters are the same for both.
    # if so, continue from that character in c till the end of the string
    
    # reverse the string and check if it's the same as the original string
    # return the result string and True/False for the check
    
    # reverse string 
    r = s[::-1]
    # use the index of the first character to find all characters in c and delete them
    for index in range(len(c)):
        char = c[index]
        # delete the characters 
        if char in s:
            s = s.replace(char,"")
    # check if the strings are the same
    if s == r:
        return True
    else:
        return False
    
    
    
