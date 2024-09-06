

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
    # Get the length of the original string
    n = len(string)

    # Initialize the reversed string
    reversed_string = string[::-1]

    # Initialize the current suffix
    current_suffix = string[n-1]

    # Reverse the string from the end
    for i in range(n-1, 0, -1):
        string[i] = string[n-i-1]
        n -= i

    # Find the longest postfix that is a palindrome
    prefix = string[0:n//2]
    if is_palindrome(prefix):
        suffix_length = n // 2
        suffix = prefix[::-1]
    else:
        suffix_length = n//2
        suffix = reversed_string[reversed_string.index(current_suffix):]

    # Append the reverse of the suffix
    string = string[:-suffix_length] + current_suffix

    return string

