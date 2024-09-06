
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
    # your code here
    c=set(c)
    i=0
    j=len(s)-1
    while i<j:
        if s[i] in c:
            i+=1
        elif s[j] in c:
            j-=1
        else:
            if s[i]!=s[j]:
                return s[:i]+s[i+1:j]+s[j+1:],False
            i+=1
            j-=1
    return s[:i]+s[i+1:],True
