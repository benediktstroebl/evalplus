

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
    if not string:
        return ''
    palindromic_suffix_len = len(string) - 1
    while palindromic_suffix_len >= 0 and is_palindrome(string[palindromic_suffix_len::-1]):
        palindromic_suffix_len -= 1
    if palindromic_suffix_len == -1:
        return string[::-1]
    prefix_len = palindromic_suffix_len + 1
    while prefix_len > 0 and not is_palindrome(string[:prefix_len]):
        prefix_len -= 1
    return f'{string[:prefix_len]}{string[palindromic_suffix_len::-1][::-1]}'
