

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
    length = len(string)
    if length == 0:
        return ''
    if length == 1:
        return string
    # Find the longest palindrome suffix.
    max_palindrome_length = 1
    for i in range(1, length):
        if is_palindrome(string[i:]):
            max_palindrome_length = i

    if length == 2:
        return string + string[:-1]
    # Find the longest palindrome prefix.
    prefix = string[:max_palindrome_length]
    max_palindrome_prefix = 0
    for i in range(max_palindrome_length - 1, -1, -1):
        if is_palindrome(prefix[:i]):
            max_palindrome_prefix = i
    return string[max_palindrome_prefix:] + string[:max_palindrome_prefix] + string[
        :-max_palindrome_prefix
    ]

