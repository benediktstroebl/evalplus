

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
        return string
    if is_palindrome(string):
        return string
    max_postfix_length = 0
    for i in range(len(string) - 1, 0, -1):
        if string[i] != '':
            if is_palindrome(string[i:]):
                return string[i:] + make_palindrome(string[:i])
            max_postfix_length = i

    return make_palindrome(string[:max_postfix_length])

