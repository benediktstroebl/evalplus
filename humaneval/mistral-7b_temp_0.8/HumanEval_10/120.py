

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
    max_len = 0
    palindrome_index = len(string) - 1
    palindrome = ''
    palindrome_suffix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            if len(string[i:]) > max_len:
                max_len = len(string[i:])
                palindrome_index = i
                palindrome_suffix = string[i:]
    return string[:palindrome_index] + palindrome_suffix[::-1]

