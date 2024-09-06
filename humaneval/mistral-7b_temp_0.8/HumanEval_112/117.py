
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
        """
        Check if a string is palindrome
        """
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True

    return s.replace(c,'').replace(c[::-1],''),is_palindrome(s.replace(c,'').replace(c[::-1],''))
