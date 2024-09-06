

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
    # Find the longest postfix of the string that is a palindrome
    palindrome_len = max(1, len(string) - len(str(string)[::-1]))

    # Append the reverse of the prefix to the end of the string
    prefix = string[:-palindrome_len]
    suffix = string[-palindrome_len:]
    reversed_string = prefix + suffix[::-1]

    return reversed_string