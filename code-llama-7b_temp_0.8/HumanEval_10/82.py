

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
    # If string is palindrome - do nothing
    if is_palindrome(string):
        return string
    # Calculate position of first non-palindrome character
    first_non_palindrome = len(string) - 1
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            prefix = string[:i]
            suffix = string[i:j]
            if is_palindrome(prefix + suffix):
                return prefix + suffix + suffix[::-1]
        first_non_palindrome = i

    return string + string[first_non_palindrome::-1]
