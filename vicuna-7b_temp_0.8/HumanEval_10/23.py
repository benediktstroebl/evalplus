

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
    # Get the shortest palindrome that starts with the input string
    prefix = string[len(string)-1:].is_palindrome()
    if not prefix:
        return string
    suffix = string[:len(string)-1]
    # Find the longest palindrome suffix that comes before the input string
    suffix_len = len(suffix)
    while suffix_len > 0 and suffix[-1] == suffix[0]:
        suffix_len -= 1
    prefix_len = len(prefix)
    suffix = prefix[:-prefix_len]
    suffix = suffix[::-1]
    return prefix + suffix

