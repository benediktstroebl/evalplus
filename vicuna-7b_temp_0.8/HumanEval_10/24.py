

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
    prefix, suffix = string.split('')
    if is_palindrome(suffix):
        suffix_reversed = suffix[::-1]
        prefix_reversed = prefix[::-1]
        return prefix + suffix_reversed + prefix_reversed
    else:
        for prefix_suffix in zip(prefix, suffix):
            if is_palindrome(prefix_suffix[::-1]):
                suffix = prefix_suffix[::-1]
                prefix = prefix_suffix[:-1]
                if is_palindrome(prefix) and is_palindrome(suffix):
                    return prefix + suffix
                else:
                    suffix_reversed = suffix[::-1]
                    prefix_reversed = prefix[:-1]
                    return prefix + suffix_reversed + prefix_reversed
        return string

