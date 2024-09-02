

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

    def find_longest_palindrome_suffix(string: str) -> str:
        start, end = 0, len(string) - 1
        while string[start] == string[end]:
            start -= 1
            end += 1
        return string[start+1:end]

    def find_shortest_palindrome_prefix(suffix: str) -> str:
        return (suffix + suffix[::-1])[1:]

    suffix = find_longest_palindrome_suffix(string)
    prefix = find_shortest_palindrome_prefix(suffix)
    return string[:-len(suffix)] + prefix + suffix
