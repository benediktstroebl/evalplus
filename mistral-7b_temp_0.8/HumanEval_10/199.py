

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

    palindrome_prefix = ''
    for i in range(len(string)):
        palindrome_prefix += string[i]
        palindrome_prefix_reversed = palindrome_prefix[::-1]
        if palindrome_prefix_reversed == palindrome_prefix:
            break
    else:
        raise ValueError('Given string is not palindrome.')

    return palindrome_prefix + string[0:i] + palindrome_prefix_reversed
