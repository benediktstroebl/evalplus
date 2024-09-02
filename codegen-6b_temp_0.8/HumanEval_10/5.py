

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

    # Start from the end of the string and work backwards.
    #  A palindrome reversed is a string that is equal from the beginning and end.
    #  Find the longest suffix that is a palindrome.
    for i in range(len(string) - 1, -1, -1):
        palindrome = string[i:][::-1]
        if is_palindrome(palindrome):
            return string[:i] + palindrome

    return string

