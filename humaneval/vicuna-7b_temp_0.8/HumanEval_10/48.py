

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
    prefix, suffix = '', string
    for i in range(len(prefix)):
        if is_palindrome(prefix[:i+1]):
            suffix += prefix[i+1:]
            prefix = prefix[:i]
        else:
            prefix += suffix[:i]
            suffix = suffix[i:]
    suffix += string[::-1]
    return prefix + suffix

