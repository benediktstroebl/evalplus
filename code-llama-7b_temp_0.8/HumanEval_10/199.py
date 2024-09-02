

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
    def find_palindrome_suffix(string: str) -> str:
        """ Find palindromic suffix of a given string """
        suffix = ''
        for index in range(len(string) - 1, -1, -1):
            if is_palindrome(string[index:]):
                suffix = string[index:]
                break
        return suffix

    suffix = find_palindrome_suffix(string)
    prefix = string[:len(string) - len(suffix)]
    return string + suffix[::-1] if suffix else prefix


