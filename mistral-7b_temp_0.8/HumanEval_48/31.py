

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
    # return not bool(re.search(r'^(?=.*[^a-zA-Z0-9])', text))
    return not bool(re.search(r'^(?=.*[^a-zA-Z0-9])', text))
    pass

