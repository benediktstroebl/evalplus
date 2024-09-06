

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
    if is_palindrome(string):
        return string
    start_index = 0
    max_len = 0
    while True:
        length = 1 + max(len(string), max_len)
        suffix = string[start_index:start_index + length]
        prefix = string[::-1][start_index - length:start_index]
        if is_palindrome(suffix) and prefix == string[::-1][start_index - length - 1:]:
            result = string[start_index:start_index + length]
            start_index += length + 1
            max_len = length
        else:
            break
    return result

