

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
    def find_palindrome_suffix(string: str, pos: int = len(string)) -> int:
        """ Find the longest palindrome suffix of a string """
        if pos == 0:
            return 0
        if string[0] == string[-1]:
            return 1 + find_palindrome_suffix(string[1:-1], pos - 2)
        return 0

    def find_palindrome_prefix(string: str, pos: int = len(string)) -> int:
        """ Find the longest palindrome prefix of a string """
        if pos == 0:
            return 0
        if string[-1] == string[pos - 1]:
            return 1 + find_palindrome_prefix(string[:pos - 2], pos - 2)
        return 0

    suffix_length = find_palindrome_suffix(string)
    prefix_length = find_palindrome_prefix(string[:-suffix_length])
    return string[:prefix_length] + string[::-1][prefix_length:
