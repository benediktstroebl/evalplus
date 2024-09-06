
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

    # calculate the length of the s string
    s_len = len(s)
    
    # for loop to iterate through the string s
    for i in range(s_len):
        
        # loop to check for each letter in c if it exists in s
        for j in range(len(c)):
            
            # if letter in c exists in s then delete it
            if s[i] == c[j]:
                s = s[:i] + s[i+1:]
                break
    # check if the result string is palindrome
    # for loop to iterate through the string
    for k in range(len(s)):
        
        # if the letter at k index is not equal to the letter at the last index of the string
        # then the string is not palindrome
        if s[k] != s[-1*(k+1)]:
            return s,False
    return s,True
