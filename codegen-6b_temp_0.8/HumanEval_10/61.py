

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
    # Find characters that make up the longest palindrome prefix
    for i in range(len(string)):
        if is_palindrome(string[:i + 1]) == True:
            break
    # Append this prefix to the end of the supplied string and reverse it
    reversed_string = string[i:][::-1]
    return string[:i] + reversed_string

