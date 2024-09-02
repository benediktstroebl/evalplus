

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

    # Find the longest palindrome prefix that is a palindrome
    substring = ''
    for i, c in enumerate(string[::-1]):
        if is_palindrome(c + string[i:len(string) - 1:]):
            substring = string[:i + 1]
            break

    # Example substring: 'aabbc'
    # Find the longest postfix of the substring that is a palindrome
    substring = substring + substring[::-1][1:]
    return substring[::-1] + substring

