

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
    return text[0] == text[-1] and is_palindrome(text[1:-1])


assert is_palindrome('aba')
assert not is_palindrome('abb')
assert is_palindrome('')
assert is_palindrome('aaaa')
assert is_palindrome('bhjskdf')
assert not is_palindrome('aabb')
assert not is_palindrome('abcd')
assert not is_palindrome('abbd')
assert is_palindrome('abaab')
assert not is_palindrome('abcab')
assert not is_palindrome('aabb')
assert not is_palindrome('abcdcba')
assert not is_palindrome('nvfghekgbhlwcssf')
assert is_palindrome('abcdcba')
assert is_palindrome('')

