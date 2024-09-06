

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
    long_palindrome = ''
    longest_palindrome = max_length = 0

    for char in string:
        if len(longest_palindrome) < max_length:
            max_length = len(longest_palindrome)
        longest_palindrome += char
        if is_palindrome(longest_palindrome):
            long_palindrome = longest_palindrome[:-1]
            break

    if len(long_palindrome) > 0:
        return long_palindrome + string[::-1]
    else:
        return ''

