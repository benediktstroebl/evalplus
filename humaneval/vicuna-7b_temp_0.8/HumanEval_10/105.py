

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
    # Find the longest postfix of the string that is a palindrome
    n = 1
    while is_palindrome(string[n:]) and string[n:].find(string[0]) == 0:
        n += 1
    if not is_palindrome(string[n:]):
        return string

    # Find the prefix of the string that comes before the palindromic suffix
    prefix = string[:n]

    # Append the reverse of the prefix to the end of the string
    return prefix + string[n][::-1]

