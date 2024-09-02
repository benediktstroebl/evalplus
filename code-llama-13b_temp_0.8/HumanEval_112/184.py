
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
    # Hash table
    c_dict = {}
    for x in c:
        c_dict[x] = 0
        
    c_dict_len = len(c_dict)
    
    # iterate the string
    for x in s:
        if x in c_dict:
            c_dict[x] += 1
    
    res_string = ""
    for x in s:
        if x in c_dict:
            if c_dict[x] > 0:
                c_dict[x] -= 1
            else:
                res_string += x
                
    if res_string == res_string[::-1]:
        return res_string,True
    else:
        return res_string,False
