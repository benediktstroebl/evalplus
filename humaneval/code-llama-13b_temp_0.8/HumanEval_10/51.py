

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

    def is_palindrome_suffix(string: str) -> bool:
        return is_palindrome(string[::-1])

    def make_palindrome_from_suffix(string: str) -> str:
        # Find the longest palindromic suffix.
        for i in range(len(string) // 2 + 1):
            if not is_palindrome_suffix(string[i:]):
                return string[i:]
        # This code is unreachable.
        assert False

    # Find the longest palindromic suffix.
    suffix = make_palindrome_from_suffix(string)
    # Find the corresponding prefix.
    prefix_index = len(string) - len(suffix)
    prefix = string[:prefix_index]
    # Create palindrome.
    return string + prefix[::-1]

