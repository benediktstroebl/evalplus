

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
        return ''

    # Find the longest palindromic suffix of the string
    longest_palindromic_suffix: str = ''
    for idx, ch in enumerate(reversed(string)):
        if is_palindrome(string[-(idx + 1):]):
            longest_palindromic_suffix = string[-(idx + 1):]
    # print(f"Longest palindromic suffix = {longest_palindromic_suffix}")

    return string + longest_palindromic_suffix[::-1]

