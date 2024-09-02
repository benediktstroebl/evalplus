

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

    # Find the longest palindrome in the string
    longest_palindrome = ''
    for i, ch in enumerate(string[::-1]):
        # Find the longest palindrome beginning with a supplied string
        if is_palindrome(string[i:]):
            longest_palindrome = string[i:]

    if not longest_palindrome:
        return string

    return string + longest_palindrome[::-1]

