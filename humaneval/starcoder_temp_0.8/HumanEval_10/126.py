

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
    # find the longest postfix of supplied string that is a palindrome
    longest_pal_index = 0
    for index in range(len(string)):
        if is_palindrome(string[index:]):
            longest_pal_index = index
    # create new string that is the original string with the palindrome appended to it
    return string + string[longest_pal_index - 1::-1]

