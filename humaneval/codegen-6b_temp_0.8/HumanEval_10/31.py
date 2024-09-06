

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
    # TODO: This algorithm really doesn't work.
    # It does not take into account other characters besides letters.
    # It compares the length of the string with itself.
    #
    # As a first implementation I made the assumption that the input string is a palindrome,
    # so the algorithm wouldn't work if the final string were not a palindrome.
    #
    # The following implementation should work though:
    length = len(string)
    for inclusive_last_char in range(length - 1, 0, -1):
        if is_palindrome(string[:inclusive_last_char]):
            return string[:inclusive_last_char] + string[::-1]
    return string

