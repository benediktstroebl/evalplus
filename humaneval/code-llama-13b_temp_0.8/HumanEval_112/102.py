
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
    t = ""
    #Check if c is longer than s
    if len(c) > len(s):
        return (s,False)
    #Make a string with all characters in c
    for i in c:
        t += i
    #Reverse c
    t = t[::-1]
    #For each character in s if it is not in c then add it to result
    for i in s:
        if i not in t:
            t += i
    #Check if result is palindrome
    if t == t[::-1]:
        return (t,True)
    else:
        return (t,False)
