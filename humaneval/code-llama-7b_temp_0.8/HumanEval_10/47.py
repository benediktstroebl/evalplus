

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
    if string == '':
        return string

    max_suffix = string[1:]
    while len(max_suffix) > 0 and is_palindrome(max_suffix):
        max_suffix = max_suffix[1:]

    if max_suffix == '':
        return string

    prefix = string[:len(string) - len(max_suffix)]
    if len(prefix) > len(max_suffix):
        prefix = prefix[:len(prefix) - len(max_suffix)]

    return prefix + max_suffix[::-1] + max_suffix
