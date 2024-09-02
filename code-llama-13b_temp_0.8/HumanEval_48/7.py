

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

    first_letter = text[0]
    last_letter = text[-1]

    if first_letter != last_letter:
        return False

    return is_palindrome(text[1:-1])

