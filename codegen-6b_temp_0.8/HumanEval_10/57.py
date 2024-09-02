

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
    if len(string) < 2:
        return string
    i = len(string) - 1
    while i:
        start = i
        i -= 1
        while not is_palindrome(string[start:i + 1]):
            i -= 1
            if i <= 0:
                return string
        string = string[:start] + string[start:i + 1][::-1] + string[i + 1:]
    return string

