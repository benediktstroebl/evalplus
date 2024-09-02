

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
        return string
    elif is_palindrome(string):
        return string
    else:
        longest_palindrome_postfix = find_longest_palindrome_postfix(string)
        prefix = string[:-len(longest_palindrome_postfix) - 1]
        return prefix + longest_palindrome_postfix[::-1]

