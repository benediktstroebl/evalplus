

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
    # Base case: if the supplied string is a palindrome, return the string itself
    if is_palindrome(string):
        return string

    # Find the longest suffix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        # Only test palindromes up to the length of supplied string
        if is_palindrome(string[-i:]):
            return string[-i:] + make_palindrome(string[:-i]) + string[-i:]

