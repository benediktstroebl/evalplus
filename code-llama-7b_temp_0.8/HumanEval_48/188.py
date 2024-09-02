

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
    if len(text) <= 1:
        return True

    first = text[0]
    last = text[-1]
    if first != last:
        return False

    return is_palindrome(text[1:-1])
