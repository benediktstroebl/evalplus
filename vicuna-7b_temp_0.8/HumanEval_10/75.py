

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
    if not is_palindrome(string):
        return string
    else:
        max_len = 1
        max_palindrome = ''
        for i in range(len(string)):
            if is_palindrome(string[i:]) and len(string[i:]) > max_len:
                max_len = len(string[i:])
                max_palindrome = string[i:].reverse() + max_palindrome
        return max_palindrome