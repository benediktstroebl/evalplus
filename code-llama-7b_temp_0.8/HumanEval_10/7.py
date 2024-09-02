

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

    # Find the longest palindrome suffix of supplied string
    palindrome_suffix = _find_longest_palindrome_suffix(string[::-1])

    # Find the longest palindrome prefix of supplied string
    palindrome_prefix = _find_longest_palindrome_prefix(string)

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + palindrome_prefix[::-1]

