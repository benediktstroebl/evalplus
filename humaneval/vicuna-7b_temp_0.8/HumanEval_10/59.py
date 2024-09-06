

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
    string = string + 'c'  # Add a character to the end of the string so that it becomes a palindrome
    palindrome = ''
    for char in string:
        if is_palindrome(char):
            palindrome += char
        else:
            palindrome += 'c'  # Append 'c' to create a palindrome
    return palindrome

