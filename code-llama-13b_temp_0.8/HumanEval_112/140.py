
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
    #return s
    n = len(c)
    l = len(s)
    i=0
    while(i<n):
        s = s.replace(c[i],'')
        i+=1
    new_string = s
    l1 = len(new_string)
    if(l1%2==0):
        s1 = new_string[0:l1//2]
        s2 = new_string[l1//2:]
        s2 = s2[::-1]
        if(s1==s2):
            return (s1,True)
        else:
            return (s1,False)
    else:
        s1 = new_string[0:l1//2]
        s2 = new_string[l1//2+1:]
        s2 = s2[::-1]
        if(s1==s2):
            return (s1,True)
        else:
            return (s1,False)
        
    return s

