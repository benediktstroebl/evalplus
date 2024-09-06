

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
    if not string:  # edge case, empty string returns empty string
        return string

    if is_palindrome(string):
        return string

    # find the longest postfix of supplied string that is a palindrome
    longest_palindrome_postfix = ''
    for i in range(len(string)):
        string_prefix = string[:i]
        if is_palindrome(string_prefix):
            if len(string_prefix) > len(longest_palindrome_postfix):
                longest_palindrome_postfix = string_prefix

    # append reverse of a string prefix that comes before the palindromic suffix
    return string + longest_palindrome_postfix[::-1]
