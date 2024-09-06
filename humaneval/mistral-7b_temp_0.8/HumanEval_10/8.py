

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
    if not string:
        return ''
    # Find the longest postfix that is palindrome
    length_of_palindromic_suffix = len(string)
    while length_of_palindromic_suffix > 0 and not is_palindrome(string[length_of_palindromic_suffix:]):
        length_of_palindromic_suffix -= 1
    # Find the shortest prefix that is palindrome
    length_of_palindromic_prefix = 0
    while length_of_palindromic_prefix < length_of_palindromic_suffix and is_palindrome(string[:length_of_palindromic_prefix]):
        length_of_palindromic_prefix += 1
    # Construct a palindrome
    return string[:length_of_palindromic_prefix] + string[length_of_palindromic_suffix:][::-1]

