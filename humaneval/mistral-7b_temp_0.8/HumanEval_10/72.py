

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
    palindrome = string[::-1]
    if not is_palindrome(palindrome):
        return make_palindrome(palindrome)

    if len(string) > len(palindrome):
        return make_palindrome(string[:len(palindrome)])

    return palindrome + string[:len(palindrome)]

