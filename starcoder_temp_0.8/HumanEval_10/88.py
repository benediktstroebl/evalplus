

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

    # Get the longest postfix of given string that is a palindrome.
    longest_postfix = ''
    start = len(string) - 1
    while start >= 0:
        if is_palindrome(string[start:]):
            longest_postfix = string[start:]
            break
        start -= 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + longest_postfix[::-1]
