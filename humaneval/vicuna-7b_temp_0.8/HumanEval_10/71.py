

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
    if len(string) == 0:
        return string
    for i in range(len(string)):
        # check if the suffix is a palindrome
        if is_palindrome(string[i:]):
            # check if the prefix is before the palindromic suffix
            prefix_len = len(string) - i - 1
            prefix = string[i:prefix_len]
            if prefix != string[::-1][prefix_len:len(string)]:
                # append the reverse of prefix to the end of the string
                return string[:prefix_len] + string[len(string) - i:]
    return string

