

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
    # 1. Find the longest postfix of the input string that is a palindrome
    max_len = len(string)
    prefix = string[0]
    palindrome = string[1:]
    while palindrome == string[::-1]:
        palindrome = string[1:]
        prefix = string[0]
        max_len = min(max_len, len(prefix) + len(palindrome))
        if len(prefix) + len(palindrome) > max_len:
            break
    if len(prefix) > 0:
        return prefix + string[::-1][::-1]
    else:
        return string[::-1]

