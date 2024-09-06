

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

    # Base cases.
    if string == '':
        return ''
    if is_palindrome(string):
        return string

    # Find longest palindromic postfix of the string.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1
    if is_palindrome(string[:i]):
        return string

    # Find longest palindromic prefix of the string.
    j = i
    while j < len(string) - 1 and not is_palindrome(string[:j + 1]):
        j += 1
    if j < len(string):
        return string[:j] + string[j + 1:][::-1]
    else:
        return string + string[::-1]

