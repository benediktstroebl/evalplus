

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

    # Find the longest palindrome in the end of given string
    for i in range(len(string) // 2, 0, -1):
        if is_palindrome(string[-i:]):
            # If a palindrome is found, it is a prefix, so we need to find the longest prefix
            # that is also a palindrome.
            prefix = string[:len(string) - i]
            if is_palindrome(prefix):
                # If a palindrome is found, it is a postfix too, so we just append a reversed
                # prefix to it to get the palindrome.
                return string + prefix[::-1]
    # If no palindrome is found, we just return the original string.
    return string
