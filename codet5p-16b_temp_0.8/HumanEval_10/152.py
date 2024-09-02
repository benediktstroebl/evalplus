

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

    palindrome_end_index = len(string) - 1
    while palindrome_end_index > 0 and not is_palindrome(string[palindrome_end_index:]):
        palindrome_end_index -= 1
    if palindrome_end_index <= 0:
        return string
    palindrome_start_index = palindrome_end_index - 1
    while palindrome_start_index >= 0 and not is_palindrome(string[:palindrome_start_index+1]):
        palindrome_start_index -= 1
    return string[:palindrome_start_index+1] + string[::-1][palindrome_start_index:]

