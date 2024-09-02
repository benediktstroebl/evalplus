

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

    # Empty string is a palindrome of length 0
    if not string:
        return ''

    # If string is a palindrome, do nothing, return the string
    if is_palindrome(string):
        return string

    # Start from the end of the string and find the longest substring that is palindrome
    for i in reversed(range(len(string))):
        if is_palindrome(string[i:]):
            # Note that i is not included, but slice does include it, so we need to add it
            return string + string[:i + 1][::-1]

    # If no substring is palindrome, return original string
    return string
