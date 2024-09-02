
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
    # # 1
    # return (s[:len(s)//2].replace("",c),s[:len(s)//2]==s[len(s)//2:][::-1])

    # 2
    r = s[:len(s)//2][::-1]
    for i in s[:len(s)//2]:
        if i in c:
            r = r.replace(i,"")
    return (r+s[len(s)//2:], r==r[::-1])
