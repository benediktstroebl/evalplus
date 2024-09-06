

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

    for postfix_length in range(len(string), 0, -1):
        prefix_length = (len(string) - postfix_length) // 2
        if is_palindrome(string[:prefix_length] + string[postfix_length:]):
            return string[:prefix_length] + string[postfix_length:] + string[prefix_length:postfix_length:-1]
    return string
