

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
    string_len = len(string)
    if string_len == 0:
        return string
    for i in range(string_len - 1, 0, -1):
        # Find the longest palindromic suffix
        suffix = string[i:i]
        while suffix == suffix[::-1]:
            i -= 1
            suffix = string[i:i]
        if suffix == string[::-1]:
            # Append the reverse of prefix that comes before suffix
            prefix = string[i:i]
            result = string[:i] + prefix + string[i:]
            return result

    return string

