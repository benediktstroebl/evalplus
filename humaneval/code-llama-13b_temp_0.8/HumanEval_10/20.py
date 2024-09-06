

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
    # We will search for the longest suffix that is a palindrome.
    # If string itself is a palindrome, we will find a suffix of same length.
    best_palindromic_suffix = ''
    # Iterate in reverse order over the supplied string.
    for i in reversed(range(len(string))):
        # Find the longest possible palindromic suffix.
        if is_palindrome(string[i:]):
            best_palindromic_suffix = string[i:]
    # Result is a concatenation of our suffix,
    # half of the prefix that comes before it and
    # reverse of the whole prefix.
    return best_palindromic_suffix + \
        best_palindromic_suffix[0] + \
        best_palindromic_suffix[0::-1]

