

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

    # Avoid zero-division error
    if len(string) < 2:
        return string

    # Reverse the string
    string_reverse = string[::-1]

    # Find the longest palindrome suffix
    for i in range(len(string_reverse) - 1, -1, -1):
        if is_palindrome(string_reverse[:i]):
            return string + string_reverse[i:]

    # If no palindromic suffix is found, append a character and try again
    return string + string[0]

