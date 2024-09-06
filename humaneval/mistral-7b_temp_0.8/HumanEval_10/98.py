

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
    # Make sure that the string is not empty and has at least 2 characters
    if not string or len(string) < 2:
        return string
    # Find the longest palindrome postfix
    while string and not is_palindrome(string):
        string = string[:-1]
    # Make sure that the string is not empty
    if string:
        # Find the shortest prefix that can be appended to the postfix to make a palindrome
        prefix = string
        while prefix and is_palindrome(prefix):
            prefix = prefix[:-1]
        # Make the string a palindrome by appending to the end the reverse of the prefix
        return string + prefix[::-1]
    return ''

