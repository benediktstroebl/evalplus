

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
    if is_palindrome(string):
        return string

    # Find the longest palindrome ending at the given position
    position = 0
    while position < len(string):
        # Test if string with given postfix is a palindrome
        palindrome = string[position:]
        if is_palindrome(palindrome):
            break
        position += 1
    else:  # If no palindrome found, then append reverse of the prefix
        return string + string[::-1]

    # Find the longest prefix of the given string that is a palindrome
    prefix = string[:position]
    while prefix:
        if is_palindrome(prefix):
            break
        prefix = prefix[1:]
    else:  # If no prefix found, then prepend reverse of the suffix
        prefix = ""

    # Append reverse of the prefix to the palindrome to get the shortest palindrome
    return prefix + palindrome[::-1]

