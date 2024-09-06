

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
    if len(string) <= 1:
        return ''
    max_suffix_len = len(string)
    max_prefix_len = 0
    string_len = len(string)
    for i in range(1, string_len):
        if is_palindrome(string[i:]):
            max_suffix_len = i
            max_prefix_len = i
            break
    for i in range(max_suffix_len + 1, string_len):
        if is_palindrome(string[i:]):
            max_suffix_len = i
        elif is_palindrome(string[:i]):
            max_prefix_len = i
            break
    return string[:max_prefix_len] + string[max_prefix_len:][::-1]
