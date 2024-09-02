

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
    # Find the longest postfix that is a palindrome
    while is_palindrome(string):
        string = string[1:]
        if len(string) > len(string[::-1]):
            break
    else:
        return string
    
    # Append the reverse of the string prefix that comes before the palindromic suffix
    string = string[:-len(string)]
    prefix_reversed = string[::-1]
    return prefix_reversed + string

