

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
    return_string = ''
    if is_palindrome(string):
        return string

    for index in range(1, len(string) + 1):
        suffix = string[-index:]
        if is_palindrome(suffix):
            return return_string + string + suffix[::-1]

        prefix = string[:-index]
        if is_palindrome(prefix):
            return return_string + prefix + suffix[::-1]

    return return_string + string + string[::-1]

