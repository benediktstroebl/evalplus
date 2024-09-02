

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
    if len(string) == 0:
        return string
    if is_palindrome(string):
        return string
    if len(string) == 1:
        return string
    if string[0] == string[-1]:
        return string[0] + make_palindrome(string[1:])
    start = string.index(string[0]) + 1
    end = len(string) - string[0].index(string[-1]) - 1
    return string[start:end] + string[0][::-1] + make_palindrome(string[end:])