

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
    longest_palindrome = max(length, key=len)
    start = 0
    for i in range(len + 1, len + longest_palindrome):
        if is_palindrome(string[i:]) and string[i:].find(string[0:i]) == 0:
            end = i + len(string[i:])
            return string[:start] + string[end - longest_palindrome:]
        start = i
    return string

