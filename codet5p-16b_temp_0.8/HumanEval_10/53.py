

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

    start_char = string[0]
    last_char = string[-1]

    postfix = string[::-1]

    palindromic_prefix = postfix[:postfix.index(last_char) + 1]

    return palindromic_prefix + start_char + last_char + palindromic_prefix[::-1]

