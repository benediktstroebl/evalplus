

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
    length = len(string)
    palindromic_suffix = find_palindromic_suffix(string)
    if length - len(palindromic_suffix) < 2:
        return string
    else:
        string_prefix = string[:length - len(palindromic_suffix)]
        return string_prefix + string[length - len(palindromic_suffix):]

