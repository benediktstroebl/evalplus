
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
    string=s
    string_length=len(string)
    count=0
    result=''
    flag=True
    for i in range(string_length):
        if string[i] in c:
            flag=False
        result+=string[i]
    if flag==True:
        print("Result is not a palindrome")
        return (result,False)
    else:
        print("Result is a palindrome")
        return (result,True)