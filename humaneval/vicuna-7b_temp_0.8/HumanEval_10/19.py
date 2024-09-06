

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
    prefix = string[::-1]
    suffix = string
    max_len = max(len(prefix), len(suffix))
    for i in range(1, max_len + 1):
        suffix_len = len(suffix) - i
        prefix_len = len(prefix) - i
        if suffix_len == 0:
            suffix = suffix[:-i]
        elif prefix_len == 0:
            prefix = prefix[:i]
        else:
            if suffix[0] != prefix[len(prefix) - prefix_len - 1]:
                suffix = suffix[:-i]
            else:
                suffix = suffix[:-i] + suffix[1:]
                prefix = prefix[:-i] + prefix[1:]
    return prefix + suffix[::-1]

