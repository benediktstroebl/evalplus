

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
        return ''
    longest_palindrome = ''
    longest_palindrome_length = 0
    for i in range(1, len(string) + 1):
        postfix = string[:i]
        prefix = string[i:]
        is_palindrome = postfix == prefix[::-1]
        if is_palindrome:
            if len(prefix) > longest_palindrome_length:
                longest_palindrome = prefix
                longest_palindrome_length = len(prefix)
    return string + longest_palind
