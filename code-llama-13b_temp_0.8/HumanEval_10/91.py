

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
        return ''

    # first, find the longest palindromic suffix
    longest_palindromic_suffix = ''
    for i in range(len(string), 0, -1):
        cur = string[:i]
        if is_palindrome(cur):
            longest_palindromic_suffix = cur
            break

    # now, find the shortest palindrome that starts with the supplied string
    return string + longest_palindromic_suffix[::-1].replace(longest_palindromic_suffix, '', 1)
