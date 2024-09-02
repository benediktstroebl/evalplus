
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

    if s is None or c is None:
        return

    s = list(s)
    c = list(c)

    # Removing the characters from s that appear in c
    for i in c:
        while i in s:
            s.remove(i)

    # Joining the remaining characters into a string
    s = ''.join(s)

    # Checking if the string is palindrome
    is_palindrome = True
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            is_palindrome = False
            break

    # Returning the string and the boolean
    return s, is_palindrome
