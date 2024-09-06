

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
    suffix_start = 0
    max_suffix_length = 1
    while len(string) - suffix_start >= max_suffix_length:
        prefix_start = 0
        prefix_end = len(string) - max_suffix_length
        max_prefix_length = 1
        while len(string) - prefix_start >= max_prefix_length:
            if is_palindrome(string[prefix_start:prefix_end]):
                max_prefix_length = max_suffix_length - max_prefix_length + 1
            else:
                prefix_start += 1

        if max_prefix_length > max_suffix_length:
            max_suffix_length = max_prefix_length
            suffix_start = prefix_end
    return string + string[:len(string) - suffix_start][::-1]

