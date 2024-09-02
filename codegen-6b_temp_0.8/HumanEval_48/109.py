

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
    return text == text[::-1]


assert is_palindrome('')
assert is_palindrome('aba')
assert is_palindrome('aaa')
assert is_palindrome('abcd')
assert not is_palindrome('zbcd')
