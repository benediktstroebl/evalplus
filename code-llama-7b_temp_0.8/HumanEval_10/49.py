

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
    # Trim trailing spaces
    string = string.rstrip()

    # Given string is already a palindrome
    if is_palindrome(string):
        return string

    # If the supplied string is empty
    if not string:
        return ''

    # Given string is not a palindrome, trim the end of the string
    # until a palindrome is found.
    for i in range(len(string), -1, -1):
        prefix, suffix = string[:i], string[i:]
        if is_palindrome(suffix):
            return f'{prefix}{suffix}{suffix[::-1]}'

