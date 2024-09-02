

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
    # find longest palindromic suffix of a given string
    suffix = string[::-1]
    while len(suffix) > 0:
        if is_palindrome(string + suffix):
            break
        suffix = suffix[1:]
    # append reverse of the prefix to the beginning of the suffix
    return suffix + string[len(string) - len(suffix):] + suffix[::-1]

