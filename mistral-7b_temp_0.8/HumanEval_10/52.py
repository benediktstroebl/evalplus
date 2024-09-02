

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

    # Find the longest postfix of supplied string that is a palindrome.
    # Algorithm idea is simple:
    # - Use sliding window to iterate suffix of the string
    # - Use is_palindrome to check if each substring is a palindrome
    # - Maximize length of the palindromic suffix
    max_length = 0
    for i in range(1, len(string)):
        if is_palindrome(string[:i]):
            if i > max_length:
                max_length = i

    # If max_length == 0, then string is not a palindrome.
    if max_length == 0:
        return string

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string[:-max_length] + string[::-1][-max_length:]

