

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
    if is_palindrome(string):
        return string

    # Find the longest postfix that is a palindrome
    pal_i = 0
    for i in range(len(string)-1, 0, -1):
        if is_palindrome(string[:i+1]):
            pal_i = i

    # Append to the end of string reverse of a string prefix
    return string[:pal_i+1] + string[pal_i+1:][::-1]

