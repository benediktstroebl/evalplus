

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

    assert is_palindrome(string), "Given string is not a palindrome!"
    palindrome_prefix = string[:len(string) - (len(string) - 1 - len(string)) // 2]
    palindrome_postfix = string[-1 - (len(string) - 1 - len(string)) // 2:]
    return palindrome_prefix + palindrome_postfix

