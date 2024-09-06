

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
    # Base case: a string with length 0 or 1 is already a palindrome.
    if len(string) < 2:
        return string
    # Find the longest postfix of supplied string that is a palindrome.
    palindrome_suffix = find_longest_palindrome_suffix(string)
    # print('Palindrome suffix: %s' % palindrome_suffix)
    if len(palindrome_suffix) == 0:
        return string + string[::-1]
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    prefix = string[:-len(palindrome_suffix)]
    return prefix + make_palindrome(prefix[::-1] + palindrome_suffix)

