

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
    string = string.lower().strip()
    prefix = ''
    max_len = 0
    for i in range(len(string)):
        prefix += string[i]
        if len(prefix) > max_len and is_palindrome(prefix):
            max_len = len(prefix)
    return prefix + string[len(string) - max_len:][::-1]

