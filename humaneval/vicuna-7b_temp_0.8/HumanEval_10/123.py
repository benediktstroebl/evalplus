

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
    palindromic_suffix = re.findall(r'[a-zA-Z]+$', string)[0]
    if len(palindromic_suffix) > 1:
        # append the reverse of the prefix that comes before the palindromic suffix
        prefix = re.findall(r'[a-zA-Z]+', string)[0]
        string += prefix[::-1] + palindromic_suffix
    else:
        string += palindromic_suffix
    return string

