
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
    str_g=len(s)
    list_s=list(s)
    list_c=list(c)
    str_s = reversed(s)
    boolean_s = True
    for i in range(str_g):
        if list_c[0] == list_s[i]:
            list_s[i] = ""
            boolean_s = False
            list_c.pop(0)
            print(list_s)
    print(boolean_s)
    print(list_c)

