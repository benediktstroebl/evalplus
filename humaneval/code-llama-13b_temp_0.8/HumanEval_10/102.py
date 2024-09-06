

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
    # Empty string is a palindrome.
    if not string:
        return ''

    # Loop through all prefixes in the string.
    # For each prefix find the longest suffix that is a palindrome.
    for length in range(len(string), 0, -1):
        prefix, suffix = string[:length], string[length:]
        if is_palindrome(suffix):
            break
    else:
        # In case of no break (no palindromic suffix found).
        length = 0

    # Now we want to reverse the prefix and add it to suffix.
    return string + prefix[::-1]

