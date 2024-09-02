

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
    string = string + 'a' if is_palindrome(string) else string
    start = max(len(string) - 1, 0)
    for end in range(start, len(string)):
        suffix = string[end:]
        if suffix == suffix[::-1]:
            continue
        suffix = suffix[::-1]
        if suffix == suffix[len(suffix) - 1:].reverse():
            return string[:end] + suffix
    return string

