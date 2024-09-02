

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
    if text is None:
        return False

    text_lower = text.lower()
    text_lower_reverse = text_lower[::-1]
    return text_lower == text_lower_reverse

