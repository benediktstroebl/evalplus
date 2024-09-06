

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

    # Find longest postfix that is a palindrome.
    i = 0
    j = 0
    while True:
        if is_palindrome(string[i:]):
            j = i
        if i == len(string):
            break
        i += 1

    # Append to the end of string reverse of a string prefix that comes before the palindromic suffix.
    return string[:j][::-1] + string

