

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
    # Find the longest prefix which is a palindrome
    longest_prefix_pal = '',
    for i in range(len(string)):
        prefix = string[:i]
        if is_palindrome(prefix):
            longest_prefix_pal = prefix, i
    # Find the shortest suffix which is a palindrome
    shortest_suffix_pal = '',
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            shortest_suffix_pal = string[i:], i
    # Return the string which begins with the longest prefix and is then reversed
    return longest_prefix_pal[0] + shortest_suffix_pal[0][::-1]
