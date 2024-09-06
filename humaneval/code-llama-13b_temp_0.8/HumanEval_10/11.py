

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
    # An empty string is a palindrome.
    if not string:
        return ''

    # A single char string is a palindrome.
    if len(string) == 1:
        return string

    # A palindrome can't be made shorter, so it is a palindrome already.
    if is_palindrome(string):
        return string

    # Expand around the middle.
    while True:
        if (
                string[:1] == string[-1:] and
                is_palindrome(string[1:-1])
        ):
            break
        string = string + string[-2::-1]

    return string
