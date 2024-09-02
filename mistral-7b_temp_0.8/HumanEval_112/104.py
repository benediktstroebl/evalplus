
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
    pal=[]
    for i in range(0,len(s)):
        for j in range(0,len(c)):
            if(s[i]==c[j]):
                s=s[:i]+s[i+1:]
                break
    if s==s[::-1]:
        pal.append(s)
        pal.append(True)
    else:
        pal.append(s)
        pal.append(False)
    return pal
