

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
    max_len = len(string)
    result = string[max_len//2:max_len]
    if is_palindrome(result):
        return result
    else:
        prefix = string[:max_len//2]
        suffix = string[max_len//2+1:]
        result = prefix + string[::-1][:len(suffix)] + suffix
        return result

