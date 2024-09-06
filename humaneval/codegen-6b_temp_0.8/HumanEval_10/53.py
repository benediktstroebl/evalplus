

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

    # Get the longest palindromic suffix => LPS
    # LPS == longest palindromic substring
    # LPS can be thought of as the furthest ending of a string suffix

    LPS = longest_palindromic_suffix(string)

    # Get the the reversed suffix
    # Example: lps = 'abc', reversed_suffix = 'cba'
    reversed_suffix = string[len(string) - len(LPS):]

    LPS += reversed_suffix[::-1]
    return LPS

