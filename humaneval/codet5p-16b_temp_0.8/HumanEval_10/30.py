

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

    suffix_length = 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            suffix_length = len(string[i:])
            break
    if suffix_length == 0:
        return string

    return string[:-suffix_length] + string[:-suffix_length][::-1]

