

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
    # longest postfix
    max_len = len(string)
    suffix = ''.join([string[i:j] for i, j in zip(range(max_len), range(max_len)) if is_palindrome(string[i:j])])

    # append reverse of prefix
    for i in reversed(range(len(suffix))):
        prefix = ''.join([string[i] for i in range(max_len)])
        if prefix not in string:
            break
        if suffix[i] != prefix[len(prefix) - i - 1]:
            break
        string = string[:len(prefix)] + string[i + len(prefix):] + string[::-1][i + len(prefix):]

    return string

