

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
    string = string.lower()

    # Find the longest suffix of the string that is a palindrome
    while len(string) > 0:
        if is_palindrome(string):
            return string
        else:
            string = string[1:]

    # the suffix that begins with string is not a palindrome
    # so start appending to the end of the supplied string
    return string + string[::-1]

