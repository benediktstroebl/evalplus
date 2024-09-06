

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
    left_palindrome = None
    for i in range(len(string)):
        if is_palindrome(string[i:]) and (not left_palindrome or len(string[i:]) > len(left_palindrome)):
            left_palindrome = string[i:].lstrip('')
            break
    if not left_palindrome:
        return string
    right_suffix = string[len(left_palindrome):]
    reverse_suffix = string[:(-1) * (len(left_palindrome) // 2)]
    return left_palindrome + reverse_suffix + right_suffix

