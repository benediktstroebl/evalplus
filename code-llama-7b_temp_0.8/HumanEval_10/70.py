

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
    if is_palindrome(string):
        return string

    for index in range(len(string) // 2):
        palindrome_suffix = string[index:-index]
        if is_palindrome(palindrome_suffix):
            palindrome_prefix = string[:index][::-1]
            return palindrome_prefix + palindrome_suffix + palindrome_prefix[::-1]

    return string[::-1]
