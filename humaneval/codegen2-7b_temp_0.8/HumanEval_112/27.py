
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
    if c=='':
        return s,True
    if s.find(c)<0:
        return s,False
    
    s_ = s[:]
    c_ = c[:]
    i,j = 0,0
    while i<len(s_):
        j = s_.find(c_,i)
        if j<0:
            return s_,True
        else:
            s_ = s_[:j] + s_[j+1:]
            i = j + 1
    return s_,
