

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

    # Iterate in reverse order over the supplied string and find the longest
    # palindromic suffix.
    rev_str = string[::-1]
    palindrom_prefix = ''
    for i in range(len(string)):
        idx = len(string) - 1 - i
        if is_palindrome(rev_str[i:]):
            palindrom_prefix = rev_str[:i]
            break

    return string + palindrom_prefix[::-1]

