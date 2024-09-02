

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
    def suffix_palindrome(string: str) -> str:
        """ Returns the shortest postfix of a string that is a palindrome """
        for suffix_len in range(1, len(string)):
            suffix = string[-suffix_len:]
            if is_palindrome(suffix):
                return suffix
        raise ValueError('No palindrome found')
    try:
        return string + suffix_palindrome(string)[::-1]
    except ValueError:
        return ''

