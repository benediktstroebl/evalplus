
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
    # Find common letters in c and s
    common = []
    for letter in c:
        if letter in s:
            common.append(letter)
    # Remove all the letters in s
    for letter in common:
        s = s.replace(letter, "")
    # Reverse the letters
    r_s = s[::-1]
    # Check if it is a palindrome
    pal = False
    if r_s == s:
        pal = True
    # Return a tuple
    return (s,pal)
