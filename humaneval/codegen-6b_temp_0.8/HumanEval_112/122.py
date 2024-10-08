
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
    # Replace this with your code
    # s = s.replace(c,"")
    # print(s)
    # print(s[::-1])
    # if s[::-1] == s:
    #     return(s[::-1],True)
    # else:
    #     return(s[::-1],False)
    back_char = s[::-1]
    front_char = s
    if back_char == front_char:
        return(back_char,True)
    else:
        return(back_char,False)
