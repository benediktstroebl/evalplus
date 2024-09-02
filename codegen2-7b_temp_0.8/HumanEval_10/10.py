

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
    palindrome_start = None
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            prefix = string[i:j]
            if is_palindrome(prefix):
                palindrome_start = prefix
                break
    if not palindrome_start:
        return string
    suffix = string[len(palindrome_start):]
    return palindrome_start + suffix[::-1]
