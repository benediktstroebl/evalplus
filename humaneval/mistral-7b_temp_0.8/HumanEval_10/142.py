

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
    if string == '':
        return ''

    # Find longest palindrome postfix
    longest_pal = string
    for idx in range(len(string) - 1, 0, -1):
        pal = string[:idx + 1]
        if is_palindrome(pal) and len(pal) > len(longest_pal):
            longest_pal = pal

    # Add the prefix of the input string reversed
    prefix = string[:len(string) - len(longest_pal)]
    return longest_pal + prefix[::-1]

