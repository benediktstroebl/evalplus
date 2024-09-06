

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
    # Initialize the original string
    original_string = string
    # Initialize a variable to store the reversed version of the original string
    reverse_string = ''
    # Initialize another variable to store the longest postfix that is a palindrome
    longest_palindrome = ''
    # Iterate through the string
    for char in string:
        # If the current char is a palindrome, append it to the reversed string
        if is_palindrome(char):
            reverse_string += char
        # If the current char is not a palindrome, look for the longest postfix that is a palindrome
        else:
            longest_palindrome = max(longest_palindrome, len(reversed(char)))
    # Append the longest palindrome to the beginning of the original string
    string = longest_palindrome + original_string[::-1]
    return string
