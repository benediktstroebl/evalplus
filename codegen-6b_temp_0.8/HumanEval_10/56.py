

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
    # This is going to be the string that we will rotate around
    rotated_string = string[- len(string):]
    # How long does rotated_string have to be?
    len_rotated = len(rotated_string)

    # Find new string that is a palindrome
    for i in range(1, len_rotated + 1):
        rotated_string = rotated_string[1:] + rotated_string[0]
        if is_palindrome(rotated_string):
            return string + rotated_string[::-1]

    return string

