

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

    # Return the string if it is a palindrome.
    if is_palindrome(string):
        return string

    # Look for the longest palindromic suffix.
    max_len = 0
    max_suffix = ''
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix) and len(suffix) > max_len:
            max_len = len(suffix)
            max_suffix = suffix

    # Append reverse of prefix to the end of the string.
    pre_len = len(string) - max_len
    prefix = string[0:pre_len]
    return prefix + max_suffix[::-1]

