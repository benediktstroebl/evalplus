

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

    def find_longest_palindrome(string):
        """ Find the longest palindrome that is a postfix of the supplied string """
        for i in range(len(string)):
            prefix = string[:i]
            suffix = string[i:]
            if is_palindrome(suffix):
                return prefix, suffix
        return string, ''

    def reverse(string):
        """ Reverse given string """
        return string[::-1]

    result = string
    prefix, suffix = find_longest_palindrome(string)
    if not is_palindrome(string):
        result = prefix + reverse(prefix) + suffix

    return result

