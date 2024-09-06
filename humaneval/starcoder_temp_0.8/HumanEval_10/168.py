

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
    # Find longest postfix that is a palindrome
    for i in range(len(string) + 1, 0, -1):
        if is_palindrome(string[-i:]):
            break
    else:
        return string
    # Find the longest prefix that comes before the palindromic postfix
    for j in range(len(string) - 1, i - 2, -1):
        if is_palindrome(string[:j]):
            break
    else:
        return string
    # Construct palindrome from prefix, string and its reverse
    return string[:j] + string + string[-i:][::-1]

