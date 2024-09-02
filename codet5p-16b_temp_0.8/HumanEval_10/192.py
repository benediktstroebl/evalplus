

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

    from itertools import takewhile

    def is_palindrome_postfix(string: str) -> bool:
        """ Return True if given string is a palindrome. """
        return string[::-1] == string

    def get_palindrome_postfix(string: str) -> str:
        """ Return the longest palindromic postfix of supplied string. """
        return ''.join(list(takewhile(is_palindrome_postfix, reversed(string))))

    if is_palindrome(string):
        return string
    postfix = get_palindrome_postfix(string)
    return string + postfix[::-1][len(postfix):]

