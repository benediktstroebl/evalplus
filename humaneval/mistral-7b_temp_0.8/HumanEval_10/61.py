

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
    reverse_prefix = ""
    # Find the longest postfix of supplied string that is a palindrome
    reverse_suffix = string
    while not is_palindrome(reverse_suffix):
        reverse_suffix = reverse_suffix[1:]
    suffix = reverse_suffix[1:]
    # Find the string prefix before the palindromic suffix
    while not is_palindrome(string[:len(suffix)]):
        reverse_prefix = string[:len(suffix)] + reverse_prefix
        string = string[:len(suffix)]
    return string + reverse_prefix + suffix

