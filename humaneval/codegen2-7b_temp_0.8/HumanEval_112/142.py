
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
    n=len(s)
    check=False
    lst_s=list(s)
    lst_c=list(c)
    for i in range(n):
        if lst_s[i]!=lst_c[0]:
            del lst_s[i]
            del lst_c[0]
            if len(lst_s)==0:
                check=True
    return "".join(lst_s),check
            
    
