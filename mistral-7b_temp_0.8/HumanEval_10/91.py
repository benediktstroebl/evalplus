

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
    # 1. Find the longest postfix of supplied string that is a palindrome
    postfix = string
    while not is_palindrome(postfix):
        postfix = postfix[:-1]

    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(postfix)]
    return prefix + postfix + prefix[::-1]

