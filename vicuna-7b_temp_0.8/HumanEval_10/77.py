

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
    if len(string) == 1:
        return string

    if not is_palindrome(string):
        return ''

    prefix_len = len(string)
    suffix_len = len(string) // 2

    suffix = string[-suffix_len:].join(string[0:suffix_len])

    postfix_len = max(prefix_len - suffix_len, 0)
    postfix = string[-postfix_len:]
    postfix = postfix.join(string[:prefix_len])

    return suffix + postfix[::-1]

