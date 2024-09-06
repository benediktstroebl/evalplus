

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
    # Handle edge cases
    if len(string) == 0:
        return ''
    if len(string) == 1:
        return string + string

    # Find longest palindrome suffix
    for i in reversed(range(len(string))):
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break
    else:
        # If palindrome not found, then string itself is a palindrome
        return string

    # Find the prefix that comes before the palindrome
    prefix = string[:i]
    return prefix + suffix[::-1] + suffix

