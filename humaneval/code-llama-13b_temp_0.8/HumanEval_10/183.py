

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

    # special case: empty string
    if string == '':
        return ''

    # get the reversed supplied string
    rev_str = string[::-1]

    # while generating reversed string,
    # check if a palindrome is found
    for i in range(len(string) + 1):
        if is_palindrome(rev_str[:len(string) - i] + string):
            return rev_str[:len(string) - i] + string

    # no palindrome found, which is equivalent to supplying an
    # string that is a palindrome by itself
    return string

