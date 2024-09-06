

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

    def make_palindrome_helper(string: str, palindrome: str) -> str:
        """ Recursive helper function to find the palindromic postfix """
        if len(string) == 0:
            return palindrome
        else:
            if is_palindrome(string):
                return string
            else:
                return make_palindrome_helper(string[1:], string[0] + palindrome)

    return string + make_palindrome_helper(string[::-1], '')

