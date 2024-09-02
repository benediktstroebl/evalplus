

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
    prefix_length = 0
    while prefix_length < len(string) and string[prefix_length] == string[-1 - prefix_length]:
        prefix_length += 1
    return string[:prefix_length] + string[-1 - prefix_length:] + string[prefix_length:-1 - prefix_length]

