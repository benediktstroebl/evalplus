

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
    # Reverse the string and search for the first occurence of it in the original string
    rev_string = string[::-1]
    pos = string.find(rev_string)
    # If the string is a palindrome already, return it
    if pos == 0:
        return string
    # Find the palindrome suffix
    palindrome_suffix = string[pos + 1:]
    # Find the palindrome prefix (everything before palindrome suffix in reverse order)
    palindrome_prefix = rev_string[1:pos + 1]
    # Combine them together
    palindrome = palindrome_suffix + palindrome_prefix
    return string + palindrome
