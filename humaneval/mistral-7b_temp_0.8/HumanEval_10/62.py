

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
    start, end = 0, len(string) - 1
    while end > start and string[start] == string[end]:
        start += 1
        end -= 1
    palindrome_length = end - start + 1
    palindrome_part = string[start:end + 1]
    start = 0
    while string[start] != palindrome_part[-1]:
        start += 1
    return (string[:start] + palindrome_part[::-1] + string[start:])[palindrome_length:]
