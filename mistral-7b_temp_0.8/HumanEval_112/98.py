
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
    #Write your code here
    tup=()
    s=s.lower()
    c=c.lower()
    if len(s)==len(c):
        c=c+s[len(c):]
        s=c
        s1=[]
        s1.append(s[0])
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                s1.append(s[i+1])
                continue
            else:
                tup=(s1,False)
                return tup
        else:
            tup=(s1,True)
            return tup
    else:
        tup=(s,False)
        return tup
