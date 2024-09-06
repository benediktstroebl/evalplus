

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
    assert type(string) is str

    start_index = 0
    end_index = len(string)
    while end_index >= start_index:
        postfix = string[start_index:]
        # find the longest palindrome string in the postfix
        suffix = postfix[::-1]
        if is_palindrome(suffix):
            return string[0:start_index + 1] + suffix
        else:
            start_index += 1

    return string
