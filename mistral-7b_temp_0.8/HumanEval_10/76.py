

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
    # 1. Find a longest palindromic postfix of string
    # palindromic postfix (if exists) always starts with string end.
    # Find the starting position (begin) of this postfix
    if string == '':
        return ''
    begin = len(string) - 1
    while begin >= 0 and is_palindrome(string[begin:]):
        begin -= 1
    # 2. Find a prefix starting with string beginning (begin) that is a palindrome
    # prefix always ends with string beginning
    end = 0
    while end < begin and is_palindrome(string[:end + 1]):
        end += 1
    return string[:begin + 1][::-1] + string[end:]

