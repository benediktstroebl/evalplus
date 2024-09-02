

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

    string_reversed = str(reversed(string))
    if is_palindrome(string_reversed):
        return string_reversed

    longest_palindrome = ''
    for prefix in string:
        if is_palindrome(prefix):
            longest_palindrome = longest_palindrome + prefix

    reversed_prefix = string_reversed[-len(longest_palindrome):]
    palindrome = longest_palindrome + reversed_prefix
    return palindrome
