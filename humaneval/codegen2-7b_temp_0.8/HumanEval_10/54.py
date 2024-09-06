

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
    palindromic_prefix = ''
    for i in range(len(string)):
        while string[:i+1]!= palindromic_prefix and string[i+1:]!= palindromic_prefix:
            palindromic_prefix += string[i+1:]
        palindromic_prefix += string[:i+1]
        if is_palindrome(palindromic_prefix):
            return palindromic_prefix
    return palindromic
