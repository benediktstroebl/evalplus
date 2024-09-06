

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
    if not string:
        return string
    else:
        start = 0
        max_len = len(string)
        while start <= max_len:
            # Find the longest palindrome that starts with the given string
            max_len = max(max_len, len(string[start:start+len(string[:start])]))
            start += len(string[:start])
        # Append the reverse of the prefix that comes before the palindromic suffix
        prefix = string[:start].reverse()
        return prefix + string[start+1:max_len]

