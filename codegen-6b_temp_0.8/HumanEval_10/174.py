

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
    # We'll need to reverse the string for the palindrome to be valid.
    # First find the longest palindromic suffix that begins with the supplied string.
    max_suffix_start = 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            max_suffix_start = i
            break
    # Use reversed() to reverse the string and return the prefix
    return string[:max_suffix_start][::-1] + string

