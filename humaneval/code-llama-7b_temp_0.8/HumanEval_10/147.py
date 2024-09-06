

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
    string_len = len(string)
    palindrome_len = string_len
    for suffix_len in range(string_len, 0, -1):
        suffix = string[-suffix_len:]
        if is_palindrome(suffix):
            palindrome_len += suffix_len
            break
    else:
        raise ValueError("Can't find palindrome")
    prefix = string[:string_len - palindrome_len]
    return f'{prefix}{suffix[::-1]}'

