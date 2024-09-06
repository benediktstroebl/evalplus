

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
    # Base case - empty string is a palindrome of any length.
    if not string:
        return string

    # Find the first index from the end of the string for which a substring
    # from the beginning to the index is a palindrome.
    for i in reversed(range(len(string) + 1)):
        if is_palindrome(string[:i]):
            break
    # Reverse the prefix before the palindromic suffix and append it to the end of the string.
    return string + string[:i][::-1]

