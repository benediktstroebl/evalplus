

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

    def reverse(s: str) -> str:
        return s[::-1]

    def find_longest_palindrome_suffix(s: str) -> str:
        for i in range(len(s)):
            if is_palindrome(s[i:]):
                return s[i:]
        return ''

    def append_prefix(s: str) -> str:
        return s + reverse(s[:-1])

    longest_palindrome_suffix = find_longest_palindrome_suffix(string)
    return append_prefix(string) if string else '' + longest_palindrome_suffix
