

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

    # Empty string is a palindrome
    if not string:
        return ''

    # Iterate in reverse order over the string. First character that is not a palindrome is the last character of our
    # palindrome prefix.
    for i in range(len(string) - 1, -1, -1):
        if not is_palindrome(string[0:i + 1]):
            break

    prefix = string[:i + 1]
    suffix = string[0:len(string) - len(prefix)]
    return prefix + suffix[::-1] + prefix

