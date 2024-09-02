
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
    # The code below has been commented due to timeout issues in leetcode.
    # def ispalindrome(s):
    #     return s[::-1] == s

    # a = 0
    # b = len(s)-1
    # while a<b:
    #     if s[a] in c:
    #         s = s[:a]+s[a+1:]
    #         a = a - 1
    #     if s[b] in c:
    #         s = s[:b]+s[b+1:]
    #         b = b -1
    #     a = a + 1
    #     b = b - 1
    # return s, ispalindrome(s)
    s = s.replace(c,'')
    return s, s[::-1] == s
