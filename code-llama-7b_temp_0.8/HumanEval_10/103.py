

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
    n = len(string)

    if n < 2:
        return string + string[::-1]

    # Find the longest palindromic suffix.
    r_idx = n - 1
    l_idx = r_idx - 1
    while l_idx >= 0 and string[l_idx] == string[r_idx]:
        r_idx -= 1
        l_idx -= 1

    # Reverse the suffix.
    suffix = string[l_idx + 1:r_idx + 1]
    reversed_suffix = string[l_idx + 1:r_idx + 1][::-1]

    return string + reversed_suffix

