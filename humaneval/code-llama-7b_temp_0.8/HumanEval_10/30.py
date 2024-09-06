

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

    # Find the longest palindrome suffix
    for suffix_start in range(len(string), -1, -1):
        prefix = string[:suffix_start]
        suffix = string[suffix_start:]
        if is_palindrome(suffix):
            return prefix + suffix[::-1]

    return string  # In case of no palindrome suffixes

