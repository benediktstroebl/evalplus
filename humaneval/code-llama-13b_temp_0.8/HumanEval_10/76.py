

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
    assert isinstance(string, str), "Argument 'string' must be of type 'str'"
    if not string:
        return ''
    if is_palindrome(string):
        return string

    longest_palindromic_suffix = ''
    for i in range(len(string)):
        current_suffix = string[i:]
        if is_palindrome(current_suffix):
            longest_palindromic_suffix = current_suffix

    # Note: It should be possible to improve the algorithm by checking for the longest palindrome not from the beginning
    # of the string, but from the current position, that is, for prefixes of decreasing length.
    prefix = string[:-len(longest_palindromic_suffix)]
    return string + prefix[::-1]

