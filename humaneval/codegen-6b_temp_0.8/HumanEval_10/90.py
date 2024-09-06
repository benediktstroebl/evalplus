

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

    # Find the longest suffix of string that is a palindrome.
    longest_suffix = max(filter(is_palindrome, suffixes(string)))
    # Create the postfix of the longest prefix with a reversed suffix.
    postfix = longest_prefix(string[:-len(longest_suffix)])[::-1]

    return postfix + longest_suffix

