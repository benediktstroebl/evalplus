

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

    def is_palindrome_substring(string: str) -> bool:
        return is_palindrome(string)

    def reverse_string(string: str) -> str:
        return string[::-1]

    def get_last_palindrome_suffix(string: str) -> str:
        """ Returns the longest postfix of given string that is a palindrome """
        i = 0
        while i < len(string) and is_palindrome_substring(string[i:]):
            i += 1
        return string[len(string) - i:]

    def get_string_prefix(string: str) -> str:
        """ Returns prefix of given string """
        return string[:len(string) - len(get_last_palindrome_suffix(string))]

    return string + reverse_string(get_string_prefix(string))

