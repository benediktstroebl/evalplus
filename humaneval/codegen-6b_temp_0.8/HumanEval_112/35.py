
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
    def is_palindrome(s):
        if len(s)==0:
            return True
        elif s[0]==s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    def remove_char(s,c):
        new_s = list(s)
        for i in range(len(s)):
            if new_s[i]==c:
                new_s[i]=""
        return "".join(new_s)
    new_c = list(c)
    for i in range(len(c)):
        new_c[i] = c[-i-1]
    new_s = remove_char(s,c)
    return (new_s,is_palindrome(new_s))