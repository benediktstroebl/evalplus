

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

    # Find the longest palindromic suffix of supplied string
    for index in reversed(range(len(string))):
        suffix = string[index:]
        if is_palindrome(suffix):
            break

    # Reverse prefix before the palindromic suffix
    prefix = string[:index]
    prefix_reverse = prefix[::-1]

    # Concatenate the palindrome suffix and prefix reverse
    return suffix + prefix_reverse

