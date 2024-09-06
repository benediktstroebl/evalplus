

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

    end_of_suffix = get_longest_suffix(string)
    start_of_prefix = string[:-len(end_of_suffix)]
    if is_palindrome(end_of_suffix):
        return start_of_prefix + end_of_suffix
    return make_palindrome(start_of_prefix + end_of_suffix)

