

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
    # first, we will compare each letter of the text
    # with its mirrored letter
    # by the use of zip() function

    return text.lower() == text[::-1].lower()
