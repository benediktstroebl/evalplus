

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
    if string == '':
        return ''
    else:
        string = string[::-1]  # reverse the string
        palindromic_suffix = string[::-1].find(string[::-1])
        suffix_len = len(string[::-1])
        prefix_len = len(string) - suffix_len
        prefix_len_max = len(string) - len(string[::-1])
        prefix = string[:prefix_len_max] if prefix_len_max > 0 else ''
        return prefix + string[prefix_len - palindromic_suffix:]

