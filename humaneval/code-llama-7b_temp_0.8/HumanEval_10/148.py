

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

    # find the longest palindrome suffix
    # len(string) + 1 is the length of a palindrome with a center of ''.
    palindrome_suffix = string[::-1]
    palindrome_center_length = 0
    while is_palindrome(string + palindrome_suffix[0:palindrome_center_length + 1]):
        palindrome_center_length += 1

    # reverse a prefix that comes before the palindromic suffix
    palindrome_prefix = string[0:len(string) - palindrome_center_length]
    palindrome_prefix_reversed = palindrome_prefix[::-1]

    return palindrome_prefix_reversed + string + palindrome_suffix

