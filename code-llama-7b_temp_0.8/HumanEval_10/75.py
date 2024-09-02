

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
    prefix = ''
    suffix = string[::-1]
    # Check if string is already palindrome
    if is_palindrome(string):
        return string
    # Check if string has only one char
    if len(string) == 1:
        return string + string[0]
    # Loop to find prefix and suffix palindromes
    for i in range(len(string)):
        prefix = string[:i + 1]
        suffix = string[i::-1]
        if is_palindrome(prefix + suffix):
            return prefix + suffix + suffix[1:]

