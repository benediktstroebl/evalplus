

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
    prefix = string[0]
    suffix = string[-1]
    suffix_len = len(suffix)
    for i in range(1, suffix_len + 1):
        i_str = prefix[-i:]
        if is_palindrome(i_str):
            return prefix + i_str + suffix
    return prefix + suffix + suffix + prefix
