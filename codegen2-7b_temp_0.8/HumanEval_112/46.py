
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
    l1=[]
    l2=[]
    for i in c:
        l2.append(i)
    for j in s:
        l1.append(j)
    for i in range(len(l2)):
        if l1.count(l2[i]) > 1:
            return (s[:i]+s[i+len(l2):],True)
    return (s,False)
