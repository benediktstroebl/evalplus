

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
    string_len = len(string)
    pre = string[0:string_len]
    prefix_len = 0
    while is_palindrome(pre):
        prefix_len += 1
        pre = string[0:string_len - prefix_len]
    suffix = string[string_len - prefix_len:]
    return pre + suffix[::-1]

