

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
    string_length = len(string)
    string = list(string)
    postfix_start = string_length - 1
    postfix = string[postfix_start]
    while postfix_start > 0 and is_palindrome(postfix):
        postfix += string[postfix_start - 1]
        postfix_start -= 1
    return f'{string[0:postfix_start + 1]}{postfix[::-1]}'

