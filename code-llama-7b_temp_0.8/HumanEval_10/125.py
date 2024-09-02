

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

    # Find longest palindrome suffix
    suffix = string[::-1]
    palindrome_suffix = string
    for i in range(2, len(suffix) + 1):
        if is_palindrome(suffix[:i]):
            palindrome_suffix = suffix[:i]
            break

    # Find shortest prefix
    prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:] + string[:i]):
            prefix = string[i:]
            break

    return prefix + palindrome_suffix + palindrome_suffix[::-1]
