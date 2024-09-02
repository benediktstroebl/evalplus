
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
    #String
    s = input()
    #String
    c = input()
    #Strip
    a = s.strip()
    #Strip
    b = c.strip()
    #Create a list
    a = list(a)
    #Create a list
    b = list(b)
    #List
    c = []
    #List
    d = []
    #Loop through the string
    for i in a:
        #Check if the string is in the list
        if i in b:
            #Append to the new list
            c.append(i)
        else:
            #Append to the new list
            d.append(i)
    #Join list
    a = "".join(d)
    #Join list
    b = "".join(c)
    #Join list
    c = a + b
    #Join list
    d = "".join(a)
    #Join list
    e = "".join(c)
    #Join list
    f = "".join(b)
    #Join list
    g = "".join
