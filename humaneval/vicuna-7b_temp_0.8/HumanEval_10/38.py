

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
    string = string.lower()
    prefix_len = len(string) // 2  # Largest power of 2 less than or equal to length of string
    prefix = string[:prefix_len]  # Prefix of the longest postfix of the supplied string that is a palindrome
    suffix = string[-prefix_len:]  # Suffix of the longest postfix of the supplied string that is a palindrome
    reversed_suffix = suffix[::-1]  # Reverse of the suffix
    reversed_prefix = prefix[::-1]  # Reverse of prefix
    new_string = prefix + reversed_suffix + suffix
    return new_string

