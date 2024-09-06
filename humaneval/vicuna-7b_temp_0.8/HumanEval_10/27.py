

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
    # use the is_palindrome function to check if the string is a palindrome
    # if the string is a palindrome, return it
    if is_palindrome(string):
        return string

    # loop through the string and check if it is a palindrome
    for i in range(len(string)):
        if is_palindrome(string[i:]) and is_palindrome(string[::-1][i:]):
            return string

    # if none of the above conditions are met, return an empty string
    return ''

