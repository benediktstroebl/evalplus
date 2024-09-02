

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
    # hint: to check palindrome, you can use the function `is_palindrome` from the module `is_palindrome`
    return is_palindrome_recursive(text, 0, len(text) - 1)

