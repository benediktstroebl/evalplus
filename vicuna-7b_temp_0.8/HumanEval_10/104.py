

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
    string = string.lower()
    prefix = string[::-1]
    suffix = string

    suffix_length = len(suffix)
    prefix_length = len(prefix)

    if suffix_length == 1:
        return prefix + suffix[::-1]

    for i in range(prefix_length, suffix_length - 1, -1):
        prefix_reversed = prefix[::-1]
        suffix_reversed = suffix[::-1]
        if prefix_reversed == suffix_reversed:
            suffix = suffix[:i] + prefix + suffix[i:]
            suffix_length = i
            prefix_length = prefix_length - i
            if suffix_length == 1:
                return prefix + suffix[::-1]
            if prefix[-1] != suffix[0]:
                prefix = prefix[:-1]
                suffix = suffix[:-1]
            suffix_reversed = suffix[::-1]
            prefix_reversed = prefix[::-1]
            suffix_reversed_len = len(suffix_reversed)
            suffix_len = len(suffix)
            if suffix_len % 2 == 0:
                suffix_reversed = suffix_reversed[::-1]
            suffix = suffix[:-suffix_reversed_len] + prefix + suffix[suffix_reversed_len:]
            suffix_length = suffix_reversed_len
            prefix_length = prefix_len - suffix_reversed_len
            if prefix_length == 1:
                return prefix + suffix[::-1]
            if prefix[-1] != suffix[0]:
                prefix = prefix[:-1]
                suffix = suffix[:-1]
            suffix_reversed = suffix[::-1]
            prefix_reversed = prefix[::-1]
            suffix_reversed_len = len(suffix_reversed)
            suffix_len = len(suffix)
            if suffix_len % 2 == 0:
                suffix_reversed = suffix_reversed[::-1]
