

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
    string_reverse = string[::-1]
    # Find the longest palindrome suffix
    i = 0
    while i < len(string) and i < len(string_reverse):
        if string[i] != string_reverse[i]:
            break
        i += 1
    postfix = string[i:]
    prefix = string[:i]
    if postfix == string_reverse:
        return string
    return prefix + postfix + postfix[::-1]
