
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
    #print(s)
    #print(c)
    #print(c.find(s[0]))
    #print(c.find(s[-1]))
    #print(c.find(s[1]))
    #print(c.find(s[-2]))
    #print(c.find(s[2]))
    #print(c.find(s[-3]))
    #print(c.find(s[3]))
    #print(c.find(s[-4]))
    #print(c.find(s[4]))
    #print(c.find(s[-5]))
    #print(c.find(s[5]))
    #print(c.find(s[-6]))

    f = [s[0],s[-1],s[1],s[-2],s[2],s[-3],s[3],s[-4],s[4],s[-5],s[5],s[-6]]
    #print(f)
    g = [c.find(f[0]),c.find(f[-
