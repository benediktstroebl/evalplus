

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
    if string == "":
        return ""

    # Find the longest palindrome suffix of the given string.
    suffix_length = 1
    while suffix_length < len(string) and is_palindrome(string[suffix_length:]):
        suffix_length += 1

    suffix = string[-suffix_length:]

    # Find the longest palindrome prefix of the given string.
    prefix_length = 0
    while prefix_length < len(string) - suffix_length and is_palindrome(string[:prefix_length + suffix_length + 1]):
        prefix_length += 1

    return string[:prefix_length] + suffix[::-1] + string[prefix_length:-suffix_length]

