

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

    # Empty string is a palindrome of itself.
    if not string:
        return ''

    # For a single symbol string this is always this symbol.
    if len(string) == 1:
        return string

    # Find the longest postfix that is a palindrome.
    longest_suffix_start = 0
    for current_index, symbol in enumerate(string):
        if is_palindrome(string[current_index::-1]):
            longest_suffix_start = current_index

    reverse_prefix = string[:longest_suffix_start][::-1]
    return string + reverse_prefix

