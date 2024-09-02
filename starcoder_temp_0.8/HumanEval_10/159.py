

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
    # Find longest suffix that is palindrome
    suffix_start = len(string) - 1
    while suffix_start >= 0:
        if not is_palindrome(string[suffix_start:]):
            break
        suffix_start -= 1
    else:
        # All symbols are palindrome, no need to change anything
        return string

    # Build palindrome out of two parts
    first_half = string[:suffix_start + 1]
    second_half = string[::-1][:len(string) - suffix_start - 1]
    return first_half + second_half
