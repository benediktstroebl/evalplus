

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

    palindromic_suffix = ''
    palindromic_suffix_length = 0
    index = len(string)
    while index > 0:
        suffix = string[:index]
        if is_palindrome(suffix):
            if len(suffix) > palindromic_suffix_length:
                palindromic_suffix = suffix
                palindromic_suffix_length = len(suffix)
            index -= 1
        else:
            index -= 1

    prefix = string[:len(string) - palindromic_suffix_length]

    return string[:len(string) - palindromic_suffix_length] + palindromic_suffix[::-1]

