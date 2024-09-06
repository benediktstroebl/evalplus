

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
    palindrome_length = 0
    longest_prefix = ''
    for prefix in string:
        longest_prefix += prefix
        if is_palindrome(longest_prefix):
            longest_prefix += prefix
            if len(longest_prefix) > palindrome_length:
                palindrome_length = len(longest_prefix)
    return longest_prefix[:-palindrome_length] + string + longest_prefix[-palindrome_length:]
