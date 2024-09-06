

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

    # skip first and last char
    for i in range(1, len(text) - 1):
        if text[i]!= text[-i - 1]:
            return False
    return True
