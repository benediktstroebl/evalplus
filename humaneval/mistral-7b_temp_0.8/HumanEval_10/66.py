

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
    string_len = len(string)
    if string_len == 0:
        return ''
    if is_palindrome(string):
        return string
    min_length = float('inf')
    prefix = None
    for i in range(string_len):
        suffix = string[i:]
        if is_palindrome(suffix) and len(suffix) < min_length:
            prefix = string[:i]
            min_length = len(suffix)
    return prefix + suffix[::-1]

