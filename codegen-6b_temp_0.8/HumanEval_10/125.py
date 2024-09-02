

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
    # Check if a string is already a palindrome
    if is_palindrome(string):
        # If a string is already a palindrome we don't need to do anything
        return string

    # Find the largest substring that is a palindrome, if any
    # We iterate backwards over the supplied string to find the largest substring of the original
    # string that is a palindrome, and we reverse the substring
    for i in range(len(string), 0, -1):
        test_string = string[:i]
        if is_palindrome(test_string):
            # We reverse the substring and return it back with the original string prepended
            return test_string[::-1] + string

    # If we reach this point, we haven't found any palindrome
    return ""

