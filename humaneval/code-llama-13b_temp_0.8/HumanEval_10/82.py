

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

    # trivial case
    if not string:
        return ''

    # find the longest palindromic suffix
    longest_pal_suffix = ''
    for i in reversed(range(len(string))):
        candidate = string[i:]
        if is_palindrome(candidate):
            longest_pal_suffix = candidate
            break

    # find the shortest palindromic prefix
    shortest_pal_prefix = ''
    for i in range(len(string)):
        candidate = string[:i + 1]
        if is_palindrome(candidate):
            shortest_pal_prefix = candidate

    # now append to the end of the string reverse of the shortest palindromic prefix
    return string + shortest_pal_prefix[::-1]

