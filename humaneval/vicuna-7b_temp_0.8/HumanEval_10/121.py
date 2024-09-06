

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
    string = string.lower()
    # Find the longest postfix of the input string that is a palindrome
    postfix_len = len(string)
    while is_palindrome(string[-postfix_len:]) and postfix_len >= 2:
        postfix_len -= 1
        string = string[:-postfix_len]

    # Append the reverse of the string prefix that comes before the palindromic suffix
    if postfix_len > 0:
        prefix_len = len(string) - postfix_len
        prefix = string[:prefix_len].lower()
        return prefix + string[postfix_len:].upper()
    else:
        return ''

