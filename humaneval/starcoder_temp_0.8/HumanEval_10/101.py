

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
    if is_palindrome(string):
        return string
    longest_suffix_start_idx = len(string)
    while longest_suffix_start_idx > 0 and is_palindrome(string[:longest_suffix_start_idx]):
        longest_suffix_start_idx -= 1
    return string[:longest_suffix_start_idx] + string[longest_suffix_start_idx:][::-1]

