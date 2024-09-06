
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
    # reverse string
    rev_str = s[::-1]
    
    # create a list
    rev_list = list(rev_str)
    
    # create a copy of the string
    rev_copy = s
    
    # loop through the copy and compare each letter to the letters in c
    # if it matches, delete the letter in the rev_list
    for i in range(0, len(rev_copy)):
        if rev_copy[i] in c:
            del rev_list[i]
    
    # convert the list back to a string
    rev_string = ''.join(rev_list)
    
    # check if the string is palindrome
    if rev_string == rev_string[::-1]:
        return (rev_string, True)
    else:
        return (rev_string, False)
    
    
