

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
    postfix_start = 0
    for i in range(1, len(string)):
        if is_palindrome(string[postfix_start:i]):
            postfix_start = i

    prefix_end = postfix_start
    while prefix_end > 0 and is_palindrome(string[0:prefix_end]):
        prefix_end -= 1

    return string[:prefix_end] + string[postfix_start::-1]

