

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
    left_idx, right_idx = 0, len(string) - 1
    while left_idx < right_idx and not is_palindrome(string[left_idx:right_idx + 1]):
        right_idx -= 1
    return string[left_idx:right_idx + 1] + string[:left_idx][::-1]

