

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
    # Split string into words, prefix and suffix
    prefix, suffix, _ = string.split()
    prefix_len = len(prefix)
    suffix_len = len(suffix)

    # Find the longest palindromic suffix
    max_suffix_len = min(prefix_len, suffix_len)
    suffix = suffix[:max_suffix_len]
    prefix = prefix[:max_suffix_len]
    while suffix == suffix[::-1]:
        suffix = suffix[:max_suffix_len-1]
    suffix = suffix[:max_suffix_len]

    # Append reverse of prefix to suffix
    suffix += prefix[::-1]
    prefix = prefix[:max_suffix_len]
    suffix = suffix[:max_suffix_len]
    return suffix
