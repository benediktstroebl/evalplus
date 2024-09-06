

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
    pal_len = 0
    for i in range(len(string)):
        pal_len += 1
        for j in range(i, len(string)):
            prefix = string[:j+1]
            suffix = string[j+1:]
            if is_palindrome(prefix + suffix):
                return prefix + suffix
            if pal_len == len(string):
                return string
    return string

