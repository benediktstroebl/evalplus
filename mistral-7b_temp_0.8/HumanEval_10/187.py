

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
    palindrome_suffix = string
    while len(palindrome_suffix) > 0 and not is_palindrome(palindrome_suffix):
        palindrome_suffix = palindrome_suffix[:-1]
    if palindrome_suffix == '':
        return string

    prefix = ''
    for i in range(len(string) - 1, 0, -1):
        prefix += string[i]
        if is_palindrome(string[i - len(palindrome_suffix) + 1:i] + prefix):
            return string[i - len(palindrome_suffix) + 1:] + palindrome_suffix + prefix

    return string + palindrome_suffix[::-1]

