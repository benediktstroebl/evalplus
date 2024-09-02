

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
    s = string
    while not is_palindrome(s):
        # find the longest palindrome suffix
        # TODO: Improve suffix finding algorithm
        i = 1
        while is_palindrome(s[:(-i)]):
            i += 1
        i -= 1
        # append reverse prefix to the palindrome suffix
        prefix = s[:len(s) - i] if i > 0 else ''
        suffix = s[:(-i)] if i > 0 else s
        s = suffix + prefix[::-1]
    return s

