

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
    n = len(string)
    palindrome = ""
    max_len = n
    while max_len >= 0:
        suffix = string[max_len:]
        prefix = string[:max_len]
        if suffix == suffix[::-1]:
            palindrome += suffix
            max_len -= 1
            break
        elif suffix.endswith(prefix):
            palindrome += suffix[::-1]
            max_len -= 1
        else:
            palindrome += prefix
            max_len -= 1
    return palindrome

