
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
    def reverse(s):
        return s[::-1]
    def is_palindrome(s):
        t=True
        for i in range(len(s)/2):
            if s[i]!=s[-i-1]:
                t=False
                break
        return t
    
    s_r=reverse(s)
    if c in s_r:
        if is_palindrome(s_r)==True:
            return s_r,True
        else:
            return s,False
    else:
        return s,False


