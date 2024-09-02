

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

    # 1. Find longest postfix of given string that is a palindrome
    for i in reversed(range(len(string))):
        if is_palindrome(string[:i+1]):
            break

    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string[:i+1] + string[:i+1][::-1]

