

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

    if len(string) == 0:
        return ''

    # Find the longest palindrome suffix
    palindrome = string[::-1]
    suffix_index = len(string) - 1
    while string[suffix_index] != palindrome[0]:
        palindrome = palindrome[1:]
        suffix_index -= 1

    return string + string[:suffix_index+1][::-1]

