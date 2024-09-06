

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
    prefix, suffix = string[0], string[::-1]
    longest_palindrome = ''
    for i, char in enumerate(string):
        new_prefix = string[:i] + suffix[:len(string)-i-1]
        if is_palindrome(new_prefix):
            if len(new_prefix) > len(longest_palindrome):
                longest_palindrome = new_prefix
    return longest_palindrome +
