

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

    # Find the longest prefix of string that is a palindrome.
    index = len(string) - 1
    while index >= 0 and not is_palindrome(string[:index + 1]):
        index -= 1

    # Append a reverse of the string prefix that is a palindrome.
    return string[:index + 1] + string[:index + 1][::-1]

