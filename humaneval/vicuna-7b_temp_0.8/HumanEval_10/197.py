

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
    m, n = len(string), len(string)
    # Check if string is a palindrome
    if is_palindrome(string):
        return string
    # Find the longest palindromic suffix
    for i in range(1, n // 2):
        if is_palindrome(string[i:]) and is_palindrome(string[i - 1:i + 1]):
            suffix = string[i:i + 1]
            break
    else:
        suffix = ''
    # Append a reverse of the prefix to get the palindrome
    prefix = string[:m // 2]
    palindrome = prefix + suffix
    return palindrome