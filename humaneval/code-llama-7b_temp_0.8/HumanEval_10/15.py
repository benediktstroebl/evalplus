

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

    # The suffix that is palindrome
    suffix = ''
    for i in range(len(string), -1, -1):
        # Test the substring from the end of the string
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break

    prefix = ''
    for i in range(len(string) - len(suffix)):
        if is_palindrome(string[:i + len(suffix)]):
            prefix = string[:i]
            break

    return suffix + prefix[::-1] + suffix

