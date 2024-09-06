

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    if text == text[::-1]:
        return True
    else:
        return False

"""
Exercise 4

Write a function that converts two strings to lower case and returns their concatenation. 
If both strings are empty, return an empty string.
"""
