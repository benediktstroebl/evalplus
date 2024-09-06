

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
    max_palindrome_length = 1
    start = string
    postfix = ''
    while max_palindrome_length < len(string):
        postfix = string[:max_palindrome_length + 1]
        if is_palindrome(postfix):
            end = string[max_palindrome_length:]
            return string + end[::-1]
        max_palindrome_length += 1
    return string + start[::-1]

