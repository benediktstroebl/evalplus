
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
    s_reversed=s[::-1]
    reversed=False
    count=0
    for i in range(len(s)):
        if s[i] in c:
            count+=1
        if s[i]==s_reversed[i]:
            reversed=True
        else:
            reversed=False
            break
    if count%2!=0:
        return (s[:i-count],False)
    else:
        return (s[:i-count],reversed)
    
    
    
