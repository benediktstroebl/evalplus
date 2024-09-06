

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
    palindrome = None
    max_len = 0

    for prefix in string:
        if is_palindrome(prefix):
            suffix = string[::-1]
            reverse_suffix = suffix[::-1].lstrip('')
            len_suffix = len(suffix)

            if len_suffix > max_len:
                max_len = len_suffix
                palindrome = prefix + reverse_suffix

    return palindrome

