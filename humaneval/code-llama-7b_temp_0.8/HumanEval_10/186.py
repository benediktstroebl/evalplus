

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
    if not string:
        return string

    # find the longest palindromic suffix of string
    len_suffix = 0
    for i in range(len(string)):
        suffix = string[i:len(string) - i]
        if is_palindrome(suffix):
            len_suffix = len(suffix)
        else:
            break

    # now cut a prefix and find the longest palindromic prefix
    len_prefix = 0
    for i in range(len(string)):
        prefix = string[:i]
        if is_palindrome(prefix):
            len_prefix = len(prefix)
        else:
            break

    # now append to the end of string reverse of the prefix
    palindrome = string + string[len_prefix:len_suffix:-1]
    return palindrome

