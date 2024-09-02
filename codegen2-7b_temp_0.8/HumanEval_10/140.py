

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
    postfix = string[::-1]
    prefix = ''
    longest_palindrome = ''
    for i in string:
        longest_palindrome = i + longest_palindrome
        if is_palindrome(longest_palindrome):
            prefix += i
    return prefix + longest_palindrome[::-1]

