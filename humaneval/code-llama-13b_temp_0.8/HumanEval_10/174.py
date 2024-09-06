

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

    # reverse string and get longest palindromic suffix
    rev_string = string[::-1]
    pal_suffix = ''
    for i in range(len(string)):
        candidate = rev_string[:i + 1]
        if is_palindrome(candidate):
            pal_suffix = candidate
    # append reverse of prefix before palindromic suffix to the end of string
    prefix_idx = rev_string.index(pal_suffix)
    prefix = rev_string[:prefix_idx]
    return string + prefix[::-1]

