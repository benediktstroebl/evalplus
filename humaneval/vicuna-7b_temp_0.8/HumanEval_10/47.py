

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
    reversed_suffix = string[-1] + string[:-1]
    prefix_len = len(reversed_suffix)
    max_len = 1
    for _ in range(1, prefix_len + 1):
        prefix = string[:prefix_len]
        if is_palindrome(prefix):
            suffix = string[-prefix_len:]
            if suffix == reversed(suffix):
                if len(suffix) >= len(reversed_suffix):
                    return prefix + suffix
                suffix = suffix[:-1] + reversed_suffix
            else:
                suffix = suffix + reversed_suffix
            reversed_suffix = suffix
            max_len = 2
            break
    return ''

