

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
    if not text:
        return True

    if not text[0].isalnum():
        return is_palindrome(text[1:])

    if text[0].lower() != text[-1].lower():
        return False

    return is_palindrome(text[1:-1])

