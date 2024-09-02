

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
    # Starting string is the input string itself
    string_prefix = string
    palindromic_suffix = ''
    while is_palindrome(palindromic_suffix) and palindromic_suffix[-1] in string:
        # Append reverse of the string prefix that comes before the palindromic suffix
        palindromic_suffix = palindromic_suffix[:-1] + string_prefix.reverse()[-len(palindromic_suffix):]
        # Find the longest postfix of the input string that is a palindrome
        string_prefix = string_prefix[:-len(palindromic_suffix)]
    return palindromic_suffix

