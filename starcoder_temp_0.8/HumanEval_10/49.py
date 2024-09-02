

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

    def find_last_palindrome_postfix(string: str, pos: int = -1) -> Tuple[int, int]:
        """ Find longest palindrome postfix starting at given position """
        for i in range(len(string) - 1, pos, -1):
            if is_palindrome(string[pos: i + 1]):
                return i, i
        return 0, 0

    def find_first_palindrome_prefix(string: str, pos: int = 0) -> Tuple[int, int]:
        """ Find longest palindrome prefix starting at given position """
        for i in range(pos, -1, -1):
            if is_palindrome(string[i: pos + 1]):
                return i, i
        return 0, 0

    last_postfix, last_postfix_pos = find_last_palindrome_postfix(string, -1)
    first_prefix, first_prefix_pos = find_first_palindrome_prefix(string, 0)
    return string[:last_postfix_pos - first_prefix_pos + 1] + string[::-1][first_prefix_pos:]
