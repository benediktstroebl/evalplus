

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

    # Find the longest palindromic suffix of the string
    suffix = string
    while suffix and is_palindrome(suffix):
        suffix = suffix[1:]

    # The palindrome is either the entire string or just the suffix
    palindrome = suffix or string

    # Find the shortest prefix that is also a palindrome
    prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            prefix = string[i:]
            break

    # The palindrome is the concatenation of the prefix and the palindromic suffix
    return prefix + palindrome[::-1]
