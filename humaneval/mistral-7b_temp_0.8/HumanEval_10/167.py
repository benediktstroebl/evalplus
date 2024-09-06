

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
    string = string.strip()
    palindromic_suffix = string[::-1]
    for i in range(len(string) - len(palindromic_suffix) + 1, 0, -1):
        if is_palindrome(string[i:i + len(palindromic_suffix)]):
            return string[:i] + palindromic_suffix + string[:i][::-1]
    return ''
