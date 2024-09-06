

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
    # Empty string is a palindrome of itself.
    if not string:
        return string

    # Supplied string is a palindrome itself.
    if is_palindrome(string):
        return string

    # Increment index i from the end of the string.
    # For each i find the longest palindromic suffix that can be formed from a part of the string.
    for i in reversed(range(len(string) + 1)):
        # Find the longest palindromic suffix of a string that starts at index i.
        suffix = string[i:]
        if is_palindrome(suffix):
            # Find how many chars should be added to the end of the string to create a palindrome.
            added_chars = len(suffix) - 1
            # Reverse the string up to the beginning of the palindromic suffix.
            rev_prefix = string[:i][::-1]
            # Add reversed prefix and palindromic suffix.
            return rev_prefix + string
    raise RuntimeError("Could not find palindrome")

