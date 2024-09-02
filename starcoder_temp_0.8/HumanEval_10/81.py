

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

    # if the string is a palindrome already, no need to do anything
    if is_palindrome(string):
        return string

    # find the longest palindromic postfix
    prefix = string
    while len(prefix) > 1:
        if is_palindrome(prefix):
            break
        prefix = prefix[:-1]

    # create a palindrome by concatenating the palindromic prefix and its reverse
    result = prefix + prefix[::-1]

    # if the created palindrome is longer than supplied string, return the original string
    if len(result) > len(string):
        return string

    return result
