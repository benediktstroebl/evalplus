

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

    length = len(text)

    for idx in range(length // 2):
        if text[idx] != text[length - idx - 1]:
            return False
    return True

