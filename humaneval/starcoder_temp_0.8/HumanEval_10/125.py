

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

    # Base case
    if len(string) <= 1:
        return string

    # Find the longest palindromic postfix
    for i in range(len(string) - 1, 0, -1):
        if is_palindrome(string[i:]):
            break

    # Find the shortest prefix before that postfix
    for j in range(i):
        if is_palindrome(string[:j + 1]):
            break

    return string[:j + 1] + string[i::-1]

