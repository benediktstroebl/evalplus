

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

    if is_palindrome(string):
        return string

    # find the longest postfix of supplied string that is a palindrome
    for end in range(1, len(string) + 1):
        substring = string[-end:]
        if is_palindrome(substring):
            break

    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    substring_reversed = substring[::-1]
    return string + substring_reversed

