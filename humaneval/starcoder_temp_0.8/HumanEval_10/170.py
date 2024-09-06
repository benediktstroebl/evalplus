

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
    # Find the longest postfix of supplied string that is a palindrome.
    # This could be done using Manacher's algorithm, but for simplicity just iterate over all possible suffixes.
    for i in range(len(string)):
        # Reverse the suffix
        reversed_string = string[::-1]
        # Check if the suffix is a palindrome
        if is_palindrome(string[i:]):
            # If the suffix is a palindrome, return the original string with the suffix appended at the end.
            return string + reversed_string[i:]
    # If there is no palindrome, return the original string.
    return string
