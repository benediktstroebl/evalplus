

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
    string = string.lower()
    original_length = len(string)

    if not string:
        return string
    longest_suffix = ''
    for i in range(1, len(string) + 1):
        longest_suffix = string[-i:] + longest_suffix
        if is_palindrome(longest_suffix):
            return longest_suffix + string
    return longest_suffix + string + string[:original_length - len(longest_suffix)
