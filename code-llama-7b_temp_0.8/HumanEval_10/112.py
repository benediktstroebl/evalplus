

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

    # find the longest palindrome suffix in O(n)
    i = 1
    while i <= len(string):
        prefix = string[:i]
        if is_palindrome(prefix):
            break
        i += 1

    # extend prefix until it is the longest prefix palindrome in O(n)
    while prefix:
        suffix = string[len(string) - len(prefix):]
        if is_palindrome(suffix):
            break
        prefix = prefix[:-1]

    # concatenate prefix and suffix
    return string + suffix[::-1]

