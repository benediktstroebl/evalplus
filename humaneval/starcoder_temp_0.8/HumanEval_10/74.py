

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
    # Find longest postfix
    for i in range(len(string), 0, -1):
        # Get current postfix, starting from the end
        postfix = string[-i:]
        # Check if the postfix is a palindrome
        if is_palindrome(postfix):
            # Get prefix of current postfix
            prefix = string[:-i]
            # Append prefix in reverse to the end of string
            return string + prefix[::-1]
