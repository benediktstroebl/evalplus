

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
        return ''
    if is_palindrome(string):
        return string

    longest_palindrome_prefix = is_palindrome(string[::-1])
    if longest_palindrome_prefix:
        return string + longest_palindrome_prefix[::-1]
    longest_palindrome_postfix = string[::-1]
    return string[:len(string) - len(longest_palindrome_postfix)] + longest_palindrome_postfix

