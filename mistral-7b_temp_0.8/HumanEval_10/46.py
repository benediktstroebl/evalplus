

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
    if not is_palindrome(string):
        return string + string[::-1]

    prefix_len = 0
    for i, char in enumerate(string):
        if i + 1 >= len(string):
            break

        if not is_palindrome(string[i + 1:]):
            prefix_len += 1
            continue

        suffix_len = len(string) - i - 1
        if suffix_len + prefix_len < len(string):
            return string[i + 1 - suffix_len:i + 1] + string[:i + 1]

    return string
