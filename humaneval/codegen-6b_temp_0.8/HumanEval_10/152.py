

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
    # find the palindrome in the supplied string backwards from the original start of the string
    for i in range(len(string) - 1, 0, -1):
        if is_palindrome(string[:i]):
            prefix = string[i:]
            palindrome = prefix[::-1]
            suffix = string[:i]
            return suffix + palindrome
    return string

