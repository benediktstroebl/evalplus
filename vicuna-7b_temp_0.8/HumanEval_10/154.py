

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
    if is_palindrome(string):
        return string
    prefix = string[:-1]
    suffix = string[1:]
    if is_palindrome(suffix) and suffix[:2] == prefix[:2]:
        return prefix + suffix[2:]
    elif len(prefix) > len(suffix):
        return prefix + suffix[2:]
    else:
        return prefix + 'a' * (len(prefix) - len(suffix)) + suffix

