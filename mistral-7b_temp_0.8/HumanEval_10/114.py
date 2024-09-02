

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
    if not string:
        return ''

    if is_palindrome(string):
        return string

    palindrome_suffix = string[::-1].find(string[::-1])

    if palindrome_suffix == -1:
        return string

    prefix = string[0:palindrome_suffix]
    return f"{prefix}{prefix[::-1]}{string[palindrome_suffix + 1:]}"
