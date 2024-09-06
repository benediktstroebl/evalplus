

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
    # step 1: get the longest palindromic suffix
    suffix_len = len(string) // 2
    prefix = string[sufix_len:sufix_len+1]
    suffix = string[sufix_len:sufix_len+1]
    prefix_reversed = string[::-1]

    # step 2: append the prefix to the end of the string
    reversed_suffix = string[:sufix_len]
    reversed_suffix = string[:sufix_len] + reversed_suffix + prefix_reversed
    string = string[:sufix_len] + string[sufix_len:] + reversed_suffix

    return string