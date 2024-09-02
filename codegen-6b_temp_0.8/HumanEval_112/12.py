
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
    s = s.lower()
    c = c.lower()
    s1 = list(s)
    s1.reverse()
    s2= ""

    for i in s1:
        if i in c:
            s1.remove(i)
            s2 += i

    s2 = s2+s1
    s3 = []
    for i in s2:
        if i not in s3:
            s3.append(i)

    s3 = "".join(s3)

    if s3 == s3[::-1]:
        return (s3,True)
    else:
        return (s3,False)

