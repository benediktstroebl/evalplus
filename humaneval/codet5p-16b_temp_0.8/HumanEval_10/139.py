

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

    longest_palindrome_prefix = ''
    i = 0
    while i < len(string) and len(string) - i > len(longest_palindrome_prefix):
        substring = string[i:]
        if is_palindrome(substring):
            longest_palindrome_prefix = substring
            i += 1
        else:
            i += 1
    new_prefix = string[0: i - len(longest_palindrome_prefix)]
    return new_prefix + longest_palindrome_prefix[::-1]

