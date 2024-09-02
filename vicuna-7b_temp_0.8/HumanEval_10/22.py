

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
    start = string_len // 2  # mid of string
    middle = start + 1
    end = string_len - 1
    start_palindrome = string[start:end]
    reverse = string[start:middle - 1] + string[middle:end]
    return string[start:middle - 1] + reverse[len(reverse):]

