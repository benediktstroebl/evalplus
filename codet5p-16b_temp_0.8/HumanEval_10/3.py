

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

    if is_palindrome(string):
        return string
    if len(string) == 0:
        return ''
    max_len = 0
    result = ''
    for index in range(len(string)):
        prefix = string[:index]
        suffix = string[index:]
        if is_palindrome(suffix) and len(prefix) > max_len:
            max_len = len(prefix)
            result = prefix
    return result + suffix

