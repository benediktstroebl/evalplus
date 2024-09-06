

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
    # Step 1: Find the longest postfix of the string that is a palindrome
    half_length = len(string) // 2
    palindrome_half = string[half_length:].is_palindrome()
    if palindrome_half:
        # Step 2: Append the reverse of the prefix to the palindrome half
        reverse_prefix = string[:half_length].reverse()
        palindrome = string[half_length:].concat(reverse_prefix)
        return palindrome
    else:
        return string
