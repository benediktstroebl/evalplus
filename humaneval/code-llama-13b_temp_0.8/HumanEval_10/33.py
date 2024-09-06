

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

    for i in range(len(string) - 1):
        # Try to expand palindrome as far as possible.
        # This is possible only if the current suffix is a palindrome.
        if is_palindrome(string[i:len(string)]):
            # Reverse the prefix and append it to the end of the string.
            return string + string[i::-1]

    # Couldn't expand palindrome, so make palindrome of the shortened string and add the lost part.
    return make_palindrome(string[1:]) + string[0]

