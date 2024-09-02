

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
    if is_palindrome(string):
        return string
    longest_postfix = find_longest_postfix(string)
    if longest_postfix is None:
        return string
    prefix = string[:-len(longest_postfix)]
    palindrome_prefix = longest_postfix[::-1]
    return prefix + palindrome_prefix

