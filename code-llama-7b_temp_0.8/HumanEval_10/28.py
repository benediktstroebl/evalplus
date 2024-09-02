

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
    # Find the longest palindrome suffix
    i = 0
    while i < len(string) / 2 and string[i] == string[-(i + 1)]:
        i += 1
    # If the whole string is palindrome, return the string
    if i == len(string) / 2:
        return string

    # Find the shortest prefix that is a palindrome
    j = 0
    while j < len(string) / 2 and string[j] == string[-(j + 1)]:
        j += 1

    return string[:-(j + 1)] + string[j::-1] + string[-(j + 1):]

