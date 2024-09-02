

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

    # Find the longest postfix of string that is a palindrome
    longest_palindromic_postfix = ''
    for i in range(1, len(string) + 1):
        if is_palindrome(string[-i:]):
            longest_palindromic_postfix = string[-i:]
        else:
            break

    # Find the prefix that comes before the palindromic suffix
    for i in range(len(string) - 1, len(longest_palindromic_postfix) - 2, -1):
        if not is_palindrome(string[:i + 1]):
            prefix = string[:i]
            break
    else:
        prefix = string

    return string + prefix[::-1]

