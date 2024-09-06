

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
    # Check if the input string is empty
    if not string:
        return string

    # Check if the input string is a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of the input string that is a palindrome
    n = len(string)
    palindrome_prefix = [string[i:i+2] for i in range(n-1)]
    longest_palindrome = "".join(palindrome_prefix)

    # Append the reverse of the prefix to the end of the string
    new_string = string + longest_palindrome[::-1]

    return new_string

