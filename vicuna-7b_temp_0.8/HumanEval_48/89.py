

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
    if len(text) < 2:
        return True
    for i in range(1, len(text)):
        if text[i:len(text) - i] != text[::-1]:
            return False
    return True