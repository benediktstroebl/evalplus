

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

    i, j = 0, len(string) - 1
    while True:
        if is_palindrome(string):
            return string
        if i == j:
            # Nothing to reverse
            return string[0] + make_palindrome(string[1:])
        i += 1
        j -= 1
        if is_palindrome(string[:i]):
            # suffix for palindrome
            return string[:i] + reverse(string[i:])
        if is_palindrome(string[j:]):
            # prefix for palindrome
            return reverse(string[:j]) + string[j:]

