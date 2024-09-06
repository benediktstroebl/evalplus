

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
    string_len = len(string)
    string_prefix = string[0]
    palindrome_suffix = string_len // 2
    for i in range(string_len):
        if string[i] == string_prefix[::-1]:
            if is_palindrome(string[:i] + string[i+1:]):
                return string[:i] + string[-1-palindrome_suffix]
    return ''
