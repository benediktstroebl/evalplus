

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
    if not string:
        return string
    longest_palindrome = string[:len(string)//2]
    for suffix in range(len(string)//2, 0, -1):
        palindrome = string[:len(string)-suffix] + longest_palindrome[::-1]
        if palindrome == string:
            return palindrome
    return longest_palindrome + longest_palindrome[::-1
