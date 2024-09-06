

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
    if len(string) == 0:
        return ""

    # Find the longest postfix of supplied string that is a palindrome.
    palindrome_length = 1
    while True:
        suffix = string[len(string) - palindrome_length:]
        if not is_palindrome(suffix):
            break
        palindrome_length += 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + string[:(len(string) - palindrome_length + 1)][::-1]

