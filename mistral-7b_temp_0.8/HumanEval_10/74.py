

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
    longest_pal = ''
    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[i:]):
            longest_pal = string[i:]
            break

    prefix = string[:len(string) - len(longest_pal)]
    return prefix + longest_pal + longest_pal[::-1]

