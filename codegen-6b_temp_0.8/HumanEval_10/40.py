

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
    # Test if the supplied string is a palindrome. If so, return it.
    if is_palindrome(string):
        return string
    # Find a palindrome that begins with the supplied string.
    for i in range(len(string)):
        prefix, suffix = string[:i], string[i:]
        for j in range(len(suffix)):
            if is_palindrome(prefix + suffix[:j]):
                return prefix + suffix[:j] + prefix + suffix[:j][::-1]
    raise ValueError('No palindrome found')

make_palindrome('a')
