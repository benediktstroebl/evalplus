

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
    # Find the longest palindromic suffix of string
    i = 1
    while len(string[:-i]) > 0:
        prefix = string[:-i]
        if is_palindrome(prefix):
            break
        i += 1
    # Reverse of prefix
    prefix_rev = prefix[::-1]
    # Append reverse of prefix to the front of palindromic suffix to construct palindrome
    return prefix_rev + string

