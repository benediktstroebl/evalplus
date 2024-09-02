

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
        return string
    suffix = string[1:]
    palindrome_suffix = find_longest_palindrome(suffix)
    if is_palindrome(string):
        return string
    if is_palindrome(palindrome_suffix):
        prefix = string[:-len(palindrome_suffix)]
        return f'{prefix}{palindrome_suffix}{prefix[::-1]}'
    return f'{string}{palindrome_suffix[::-1]}'

