

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

    # Will store longest palindromic suffix
    suffix = ''
    # Will store chars that come before palindromic suffix
    prefix = ''

    # Iterate backwards over the string
    for i in reversed(range(len(string))):
        # Is the suffix palindrome?
        if is_palindrome(suffix + string[i]):
            # If so, then store the prefix
            prefix = string[:i]
            # And update the suffix
            suffix = string[i:]

    # Append to the end of the string the reverse of the prefix
    return string + prefix[::-1]

