

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

    def _longest_palindrome(string: str) -> str:
        if not string:
            return ''

        longest_palindrome = ''
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                if len(string[i:]) > len(longest_palindrome):
                    longest_palindrome = string[i:]
        return longest_palindrome

    if not string:
        return ''

    prefix = ''
    for i in range(len(string)):
        prefix += string[i]
        if is_palindrome(string[i:]):
            break

    return prefix + _longest_palindrome(string[:i][::-1])[::-1]

