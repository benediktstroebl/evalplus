
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
    char_list = list(s)
    for char in c:
        if char in char_list:
            char_list.remove(char)
    reverse_char_list = char_list[::-1]
    if char_list == reverse_char_list:
        return ''.join(char_list), True
    return ''.join(char_list), False
