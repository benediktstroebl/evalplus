

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
    if len(string) == 0:
        return string

    longest_palindromic_suffix = ''
    for i in reversed(range(len(string))):
        substring = string[i:]
        if is_palindrome(substring):
            if len(substring) > len(longest_palindromic_suffix):
                longest_palindromic_suffix = substring

    prefix = string[:len(string) - len(longest_palindromic_suffix)]
    return f'{prefix}{longest_palindromic_suffix[::-1]}'
