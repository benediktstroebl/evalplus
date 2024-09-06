

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
    def append_reverse(string: str, postfix: str) -> str:
        """ Append reverse of a string prefix that comes before the palindromic suffix.
        >>> append_reverse('', '')
        ''
        >>> append_reverse('', 'c')
        'c'
        >>> append_reverse('', 'ca')
        'cac'
        """
        return string + string[len(postfix):]

    #
