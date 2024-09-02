

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
    assert isinstance(string, str), 'input is expected to be a string'
    if len(string) <= 1:
        return string
    # find longest postfix of supplied string that is a palindrome
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[:i]):
        i -= 1
    return string + string[i-1::-1]

