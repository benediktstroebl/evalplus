

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
    # check if string is empty
    if not string:
        return string

    # check if string is a palindrome
    if is_palindrome(string):
        return string

    # find the longest palindrome prefix
    prefix_len = 1
    prefix = string
    while prefix:
        if is_palindrome(prefix):
            prefix_len += 1
        prefix = prefix[::-1]

    # append the reverse of the prefix to the string
    string_rev = string[::-1]
    return prefix[:prefix_len] + string_rev + prefix[-prefix_len:]

