

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
    n = len(string)
    while n > 0 and is_palindrome(string[n-1:n-1]):
        n -= 1
    prefix = string[:n]
    suffix = string[n:]
    prefix_reversed = string[::-1][::-1]
    suffix_reversed = string[::-1]
    reversed_suffix = string[:n]
    # Append the reversed suffix to the prefix to form a palindrome
    result = prefix + suffix_reversed + reversed_suffix
    return result

