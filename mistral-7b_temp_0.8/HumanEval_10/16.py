

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
    if string == '':
        return ''

    # keep longest palindromic postfix that starts from the end
    max_pal_postfix_length = 1
    longest_pal_postfix = string[-1]

    for i in range(1, len(string)):
        suffix = string[-i:]
        if is_palindrome(suffix):
            if len(suffix) > max_pal_postfix_length:
                max_pal_postfix_length = len(suffix)
                longest_pal_postfix = suffix

    # remove all palindromic postfixes
    string = string[:-max_pal_postfix_length]

    # keep longest palindromic prefix that ends before the last palindromic postfix
    max_pal_prefix_length = len(string)
    longest_pal_prefix = ''

    for i in range(len(string)):
        prefix = string[:i+1]
        if is_palindrome(prefix):
            if len(prefix) > max_pal_prefix_length
