

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
        return ''
    longest_palindromic_suffix_start = 0
    for i in range(1, len(string)):
        if is_palindrome(string[i:]) and i > longest_palindromic_suffix_start:
            longest_palindromic_suffix_start = i
    return string + string[longest_palindromic_suffix_start-1::-1]

