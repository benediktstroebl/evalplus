

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

    # reverse supplied string and add an extra string at the end that
    # is a reverse of a prefix
    reverse_string = string[::-1] + string

    for i in range(len(string)):
        # find the longest suffix of reverse string that is a palindrome
        if is_palindrome(reverse_string[i:]):
            return reverse_string[i:]

