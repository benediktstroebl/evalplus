

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

    # check is string is empty or consists of 1 character
    if len(text) < 2:
        return True

    # reverse string and check if it is the same as original
    return text == text[::-1]

