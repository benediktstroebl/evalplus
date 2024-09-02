

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
    if len(string) < 2:
        return string
    # Find the longest postfix of supplied string that is a palindrome or return the string if it is
    prefix, postfix = '', ''
    for i in reversed(range(len(string))):
        if is_palindrome(string[i:]):
            postfix, prefix = postfix + string[i:], prefix + string[:i]
            break
    return prefix + postfix[::-1]

