

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
    if not string:
        return ''

    max_palindrome_len = 1
    postfix_palindrome = string[0:1]
    for i in range(1, len(string) // 2 + 1):
        if is_palindrome(string[i:]):
            postfix_palindrome = string[i:]
            max_palindrome_len = len(postfix_palindrome)

    return string[:len(string) - max_palindrome_len] + postfix_palindrome[::-1]
