

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
    # Find the longest postfix of the string that is a palindrome
    palindrome_len = max(len(s) for s in set(string))
    # Append the reverse of the prefix of the string to the end of the string
    return string[:-palindrome_len] + string[palindrome_len:-palindrome_len]

