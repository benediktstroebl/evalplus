

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
    # 1. Find the longest postfix of supplied string that is a palindrome.
    # If supplied string is not a palindrome, it is obvious that there is no palindrome, so we return it as is.
    if not is_palindrome(string):
        return string

    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    prefix_length = get_longest_prefix(string)
    return string + string[:len(string) - prefix_length][::-1]

