

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
    # Reverse string and compare it with the original one
    reversed_string = string[::-1]
    if is_palindrome(string + reversed_string):
        return string + reversed_string

    # Find the longest palindrome suffix
    longest_suffix = ''
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            if len(suffix) > len(longest_suffix):
                longest_suffix = suffix

    # Find the shortest prefix that comes before a palindromic suffix
    longest_prefix = ''
    for i in range(len(string) - len(longest_suffix)):
        prefix = string[:i + 1]
        if is_palindrome(prefix + longest_suffix):
            if len(prefix) > len(longest_prefix):
                longest_prefix = prefix

    return longest_prefix + longest_suffix + longest_prefix[::-1]
