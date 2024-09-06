

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

    def find_longest_suffix(string: str) -> str:
        """ Find the longest palindromic suffix of a given string """
        suffix = string
        while len(suffix) > 0 and is_palindrome(suffix):
            suffix = suffix[1:]
        return suffix

    def find_longest_prefix(string: str) -> str:
        """ Find the longest prefix that is a palindrome """
        prefix = string
        while len(prefix) > 0 and is_palindrome(prefix):
            prefix = prefix[:-1]
        return prefix

    suffix = find_longest_suffix(string)
    prefix = find_longest_prefix(string)

    return string + suffix[::-1] + prefix[::-1]

