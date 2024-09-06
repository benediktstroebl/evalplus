

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
    # Make sure input string is not empty
    if not string:
        return string

    # Find the longest postfix of the supplied string that is a palindrome
    i = len(string) - 1
    while i >= 0:
        if is_palindrome(string[:i + 1]):
            break
        i -= 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[:i + 1][::-1]

