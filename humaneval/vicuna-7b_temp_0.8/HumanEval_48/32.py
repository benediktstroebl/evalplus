

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
    if len(text) == 2:
        return text == text[::-1]
    return not any(c != text[i::-1] for i in range(len(text)))