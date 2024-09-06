

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
    palindrome_suffix = string[::-1]
    palindrome_suffix_length = 0
    for i, char in enumerate(string[::-1]):
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            palindrome_suffix_length = len(palindrome_suffix)
            break
    return string[:-palindrome_suffix_length] + palindrome_suffix[::-1]
