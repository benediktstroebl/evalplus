

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
    prefix = []
    suffix = []
    for i in range(len(string)):
        if is_palindrome(string[i:i+2]):
            prefix.append(string[i:i+2])
        else:
            suffix.append(string[i])
        if len(prefix) > len(suffix):
            prefix.pop()
            suffix = suffix[:-1]
    suffix.append(string[i:])
    return ''.join(prefix) + string[i:i+len(suffix)]

