
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

    # 1. reverse the string
    reverse = s[::-1]
    # 2. list out all characters in string c
    # 3. compare all characters in reverse of string s with characters in list c
    # 4. if match, then delete
    # 5. reverse the string and check if the string is palindrome
    # 6. return the result

    for x in c:
        reverse = reverse.replace(x, '')

    if reverse == reverse[::-1]:
        return (reverse, True)
    else:
        return (reverse, False)
