

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
    palindrome_prefix = ''
    palindrome_suffix = ''

    for i in range(0, length):
        suffix_is_palindrome = is_palindrome(string[i:])
        prefix_is_palindrome = is_palindrome(string[:i + 1])
        if suffix_is_palindrome:
            palindrome_suffix = string[i:]
            palindrome_prefix = string[:i]
            break
        if prefix_is_palindrome:
            continue
        else:
            break
    return palindrome_prefix + string + palindrome_suffix[::-1]

