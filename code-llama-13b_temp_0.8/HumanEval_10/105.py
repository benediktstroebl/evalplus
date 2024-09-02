

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

    # we are adding one symbol at the end, so we can skip the last symbol
    for i in reversed(range(1, len(string))):
        if is_palindrome(string[i:]):
            # reverse first i symbols
            return string + ''.join(reversed(string[:i]))

    # if we got here, the string was empty or a palindrome
    return string

