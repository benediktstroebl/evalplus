

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
    if not string:
        return string
    # Find the longest palindrome suffix
    i = 1
    while len(string) - i >= i:
        substring = string[len(string) - i:]
        if is_palindrome(substring):
            break
        i += 1
    # Prepend to the reverse of the prefix a substring that comes before the palindromic suffix
    return string[:len(string) - i] + string[:len(string) - i][::-1] + substring

