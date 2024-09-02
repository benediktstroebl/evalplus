

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
        return string
    else:
        longest_palindrome = max(len(re.findall(r'\w+', string)), len(string))
        reversed_prefix = string[::-1]
        prefix = string[:longest_palindrome]
        suffix = string[longest_palindrome:]
        reversed_suffix = suffix[::-1]
        palindrome = prefix + reversed_prefix + suffix + reversed_suffix
        return palindrome

