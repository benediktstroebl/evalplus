

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
    if len(string) == 0:
        return string
    for prefix in string:
        if is_palindrome(prefix):
            suffix = string[::-1]
            suffix_len = len(suffix)
            if suffix_len >= len(prefix) - len(suffix) and suffix[0] != prefix[-1]:
                result = prefix + suffix[::-1]
                if is_palindrome(result) and len(result) > len(suffix):
                    return result
    return string

