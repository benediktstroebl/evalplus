

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

    length = len(string)
    postfix = ''
    for i in range(length - 1, -1, -1):
        postfix = postfix + string[i]
        if is_palindrome(postfix):
            break

    if not is_palindrome(postfix):
        return string + postfix[::-1]

    return string + postfix[::-1][:length - i - 1]

