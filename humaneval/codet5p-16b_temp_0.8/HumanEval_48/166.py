

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

    if len(text) <= 1:  # empty string, or a single character
        return True
    first_char = text[0]
    last_char = text[-1]
    return first_char == last_char and is_palindrome(text[1:-1])

