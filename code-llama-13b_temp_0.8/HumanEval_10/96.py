

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
    # go backwards from the end of string to see if there is palindrome
    for i in reversed(range(len(string) + 1)):
        if is_palindrome(string[0:i]):
            # if palindrome is found - append to its end the reverse of its prefix
            return string[0:i] + string[::-1]
    return ''

