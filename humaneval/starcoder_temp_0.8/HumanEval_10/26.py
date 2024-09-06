

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
    length = len(string)
    if length == 0:
        return string

    # Find the longest prefix of the string that is a palindrome
    for idx in range(length - 1, 0, -1):
        if is_palindrome(string[:idx]):
            break

    # Get the prefix of the string that we found, and append it to the end
    # of the string in reverse order
    return string[:idx] + string[idx:][::-1]
