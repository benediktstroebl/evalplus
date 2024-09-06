

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

    # Check for edge case
    if not string:
        return string

    # Check if the string is already palindrome.
    if is_palindrome(string):
        return string

    # Initialize reverse string as an empty string.
    reverse = ""

    # Iterate from last to first character in a string.
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
        # If the palindrome is found, append rest of the string to the palindrome and return
        if is_palindrome(reverse):
            return reverse + string[i+1:]

    return reverse + string

