

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
    while True:
        if is_palindrome(string):
            return string
        # Find the longest palindrome prefix.
        for i in range(len(string)):
            prefix = string[:i+1]
            if is_palindrome(prefix):
                break
        # Reverse the prefix and append it to the end of the string.
        prefix_reversed = prefix[::-1]
        return string[:i+1] + prefix_reversed
