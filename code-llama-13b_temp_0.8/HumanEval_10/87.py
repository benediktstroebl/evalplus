

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    assert len(string) >= 0, "Input string must be non-empty"
    n = len(string)

    for i in range(n - 1):
        prefix = string[:n - i]
        suffix = string[i + 1:]
        if is_palindrome(prefix) and is_palindrome(suffix):
            return string + suffix[::-1]
    return string + string[::-1]

