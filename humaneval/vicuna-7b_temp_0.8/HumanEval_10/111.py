

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
    # Step 1: find longest postfix of prefix
    prefix = string
    max_len = 0
    while prefix and is_palindrome(prefix):
        prefix = prefix[:-1]  # remove last character
        max_len = max(max_len, len(prefix))
    if prefix:
        suffix = prefix[::-1]
        return suffix + string[1:].split(suffix)[0]
    else:
        return string[::-1]

