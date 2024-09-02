

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
    len_string = len(string)
    # Fast way to find the longest palindrome postfix of a string
    max_palindrome_size = len_string // 2

    # Iterate over string prefixes until a palindrome is found
    for prefix_len in range(max_palindrome_size, -1, -1):
        # If a prefix of current length is a palindrome then return its reversed form
        if is_palindrome(string[:prefix_len]):
            return string + string[:prefix_len][::-1]
    return ''
