

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
    prefix, suffix = string[:-1], string[-1]
    prefix_is_palindrome = is_palindrome(prefix)
    suffix_is_palindrome = is_palindrome(suffix)
    if prefix_is_palindrome and suffix_is_palindrome:
        return string
    longest_prefix_postfix = ''
    for i in range(1, len(string)):
        prefix = string[:-i]
        if is_palindrome(prefix):
            longest_prefix_postfix = prefix
            break
    if longest_prefix_postfix:
        return longest_prefix_postfix + suffix
    return prefix + suffix

