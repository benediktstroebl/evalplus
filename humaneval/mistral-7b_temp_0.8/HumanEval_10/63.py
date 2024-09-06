

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
    # Find the longest postfix of string that is a palindrome
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1
    # Find the prefix that comes before the palindromic suffix
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1
    return string[j:i] + string[i:][::-1]
