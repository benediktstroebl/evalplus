

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
    n = len(string)

    # Test trivial cases
    if n <= 1:
        return string

    # Get the longest palindrome suffix of supplied string
    s = string[::-1]
    pal_suffix = ''
    for i in range(n):
        if is_palindrome(string[i:]):
            pal_suffix = string[i:]
            break

    # Reconstruct the palindrome
    prefix = string[:n - len(pal_suffix)]
    return prefix + pal_suffix[::-1]

