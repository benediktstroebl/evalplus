
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
    def can_delete(s, c):
        """
        Checks whether all characters in s can be deleted without breaking the string
        """
        for i in range(len(s)):
            if s[i] != c[i % len(c)]:
                return False
        return True
    
    # Reverse s and c, so we can iterate over them both in the same order
    s = s[::-1]
    c = c[::-1]
    
    # Check if s and c are empty
    if not s and not c:
        return ('', False)
    
    # If not, remove characters from s until we find one that is not in c
    result = s[:]
    while can_delete(result, c):
        result = result[1:]
    
    # Check if the result is palindrome
    if s == result[::-1]:
        return (result, True)
    else:
        return (result, False)
