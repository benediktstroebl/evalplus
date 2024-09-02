

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
    # reverse the string suffix
    suffix = ''.join(reversed(string))
    # reverse the string prefix
    prefix = ''
    for char in string:
        prefix += char
    # compare the suffix and prefix to check if it is a palindrome
    if is_palindrome(suffix):
        return prefix + suffix
    else:
        return suffix + prefix

