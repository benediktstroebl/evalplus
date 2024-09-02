

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
        return string

    # find the longest palindrome suffix
    suffix = string
    while suffix and is_palindrome(suffix):
        suffix = suffix[1:]

    # if suffix is not a palindrome, append reverse prefix to the string
    prefix = string[:len(string) - len(suffix)] if suffix else ''
    return suffix + prefix[::-1] + suffix

