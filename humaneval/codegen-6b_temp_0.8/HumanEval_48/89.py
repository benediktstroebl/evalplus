

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
    # a palindrome is a string that reads the same forwards and backwards.
    # 'a' == 'a', 'b' == 'b' etc.
    return text == text[::-1]

