

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
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    if text == text[::-1]:
        return True
    else:
        return False
