

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
    prefix_len = max(0, len(string) - max(0, len(string) // 2))
    prefix = string[prefix_len:]
    if is_palindrome(prefix):
        suffix = prefix[::-1]
        return prefix + suffix

    # If prefix is not a palindrome, reverse prefix and append it to the string
    suffix = string[:-len(prefix)]
    if is_palindrome(suffix):
        prefix = suffix[::-1]
        return prefix + string

    return string

