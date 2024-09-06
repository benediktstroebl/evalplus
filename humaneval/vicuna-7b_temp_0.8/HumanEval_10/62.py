

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
    string_chars = string.upper()
    for i in range(len(string_chars) // 2, -1, -1):
        prefix = string_chars[:i]
        suffix = string_chars[i:]
        if is_palindrome(suffix):
            suffix_len = len(suffix)
            prefix_len = len(prefix) + suffix_len
            new_string = prefix + suffix[::-1]
            if len(new_string) == prefix_len:
                return new_string
    return ''

