

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
    if is_palindrome(string):
        return string

    string_length = len(string)
    palindromic_suffix = string[::-1]
    for i in range(string_length):
        if is_palindrome(string[i:]):
            return string + palindromic_suffix[:i]

    raise RuntimeError(f'cannot find a palindrome prefix for the supplied string: {string}')

