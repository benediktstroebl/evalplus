

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
    if is_palindrome(string):
        return string
    max_i, max_len = 0, 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            max_i, max_len = i, len(string[i:])
    return string[:max_i] + string[:max_i][::-1] + make_palindrome(string[max_i+max_len:])
