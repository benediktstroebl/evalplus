

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
    string = string.strip()
    postfix_start = 0
    while postfix_start < len(string) and not is_palindrome(string[postfix_start:]):
        postfix_start += 1
    if not postfix_start:
        return string
    prefix_end = postfix_start
    while prefix_end and not is_palindrome(string[:prefix_end]):
        prefix_end -= 1
    return string[:prefix_end] + string[postfix_start:][::-1]

