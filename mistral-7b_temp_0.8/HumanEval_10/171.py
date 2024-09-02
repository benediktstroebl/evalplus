

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
    if is_palindrome(string):
        return string
    palindrome_postfix_length = get_longest_palindrome_postfix_length(string)
    palindrome_postfix = string[-palindrome_postfix_length:]
    palindrome_prefix = string[:-palindrome_postfix_length]
    palindrome_prefix_reverse = ''.join(reversed(palindrome_prefix))
    return palindrome_postfix + palindrome_prefix_reverse

