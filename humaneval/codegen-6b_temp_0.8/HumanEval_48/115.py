

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
    # first, truncate string at middle
    text = text.replace(' ', '')
    # then reverse string
    rev = text[::-1]
    # check if reversed string is the same as original
    if rev == text:
        return True
    else:
        return False

