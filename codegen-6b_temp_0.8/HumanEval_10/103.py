

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
    postfix = 0
    for k in range(len(string) - 1, 0, -1):
        if is_palindrome(string[:k]):
            postfix = k
            break
    if postfix == 0:
        return string + string[::-1]
    return string + string[::-1][:postfix][::-1]

