

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
    for i in range(len(string)):
        # reverse() returns a new list, and it is much faster than [::-1]
        # because it works only with lists, not with strings
        # [::-1] works with strings, but is slower than reverse()
        postfix = string[::-1]
        if is_palindrome(postfix[:i + 1]):
            return string + postfix[:i + 1][::-1]

