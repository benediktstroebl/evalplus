

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
    if len(string) <= 1:
        return string
    left, right, lenght = 0, 0, 0
    for i in range(len(string)):
        if is_palindrome(string[i:]) and lenght < len(string[i:]):
            left, right = i, i + len(string[i:])
            lenght = len(string[i:])
    return string[:left] + string[left:][::-1] + string[-right:]

