

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

    # Search for the longest palindrome postfix in the string
    i = 1
    while is_palindrome(string[:i]):
        i += 1
    palindrome = string[:i]
    assert is_palindrome(palindrome)

    # Reverse the string prefix and concatenate it with the found palindrome
    string_prefix = string[:i]
    string_prefix = string_prefix[::-1]
    return string_prefix + palindrome

