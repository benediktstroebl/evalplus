

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

    rev_str = string[::-1]
    if is_palindrome(string):
        return string

    if is_palindrome(rev_str):
        return rev_str + string

    prefix = ''
    suffix = ''
    for i in range(1, len(string)):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(prefix + suffix):
            break

    return suffix + prefix + suffix[::-1]

