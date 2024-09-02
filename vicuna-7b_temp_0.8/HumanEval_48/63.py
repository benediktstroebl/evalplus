

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
    if len(text) == 1:
        return True
    for i in range(len(text) - 1):
        if text[i] != text[i + len(text) // 2]:
            return False
    return True