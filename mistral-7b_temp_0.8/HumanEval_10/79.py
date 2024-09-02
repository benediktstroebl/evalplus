

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
        return ''
    pal_suffix_len = 0
    suffix = ''
    for i in range(1, len(string) + 1):
        suffix = string[len(string) - i:len(string)]
        if is_palindrome(suffix):
            pal_suffix_len = i
            break
    if pal_suffix_len == 0:
        return ''
    # reverse string prefix
    prefix = string[0:len(string) - pal_suffix_len]
    return prefix + suffix + suffix[::-1]

