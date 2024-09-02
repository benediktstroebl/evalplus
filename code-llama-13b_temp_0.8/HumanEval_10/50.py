

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
    rev_str = string[::-1]

    for index, ch in enumerate(string):
        rev_prefix = rev_str[:index]
        rev_suffix = rev_str[index:]

        if is_palindrome(rev_prefix) and is_palindrome(rev_suffix):
            return string + rev_suffix[::-1]

    return string + string[::-1]
