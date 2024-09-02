

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
    # make sure it's a string
    if not isinstance(string, str):
        raise TypeError("String expected")
    if len(string) == 0:
        return string
    # find longest palindrome postfix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[:i+1]):
        i -= 1
    # append prefix of reversed string
    prefix = string[i+1:]
    return prefix + string[:i][::-1]

