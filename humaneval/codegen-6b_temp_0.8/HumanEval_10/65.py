

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
    palin_suffix = get_longest_palindromic_suffix(string)
    rev_prefix = string[:-len(palin_suffix)]
    rev_suffix = rev_prefix[::-1]
    return string + rev_suffix[len(rev_suffix) - len(palin_suffix):][::-1]

