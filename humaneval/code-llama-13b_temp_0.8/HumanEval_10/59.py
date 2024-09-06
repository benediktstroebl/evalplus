

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
    # index of the first char in reverse string
    last_idx = len(string) - 1
    # index of the last char in reverse string
    first_rev_idx = 0

    # iterate the reversed string and find the longest palindromic suffix
    for idx, ch in enumerate(reversed(string)):
        if string[last_idx - idx] != ch:
            # first mismatching character
            first_rev_idx = last_idx - idx + 1
            break

    # while the first char in the reversed string is the same as in the original string
    while first_rev_idx > 0 and string[first_rev_idx - 1] == string[last_idx]:
        first_rev_idx -= 1
        last_idx -= 1

    # append reversed prefix to the end of the string
    return string + string[first_rev_idx:last_idx + 1][::-1]

