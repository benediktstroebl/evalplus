
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

    # s = "abcde", c = "ae"
    # s = "abcdef", c = "b"
    # s = "abcdedcba", c = "ab"

    def reverse_str(s):
        return s[::-1]

    # reverse_str("abc") --> "cba"
    # reverse_str("A man, a plan, a canal: Panama") --> "amana!nalp a ,lanac: Panama"

    # slice remove the first and last character in string
    s = s[1:len(s)-1]

    # s = "abcdef"
    # c = "b"

    if len(s) > len(c):
        for i in range(0,len(s)-1):
            if s[i] == c[0]:
                s = s.replace(s[i],'')
        return (s,s == reverse_str(s))
    else:
        return s,False
