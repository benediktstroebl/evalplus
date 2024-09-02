

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
    if len(string) == 0:
        return ""

    # Find the longest palindrome postfix of the string
    palindrome = ""
    for i in range(len(string)):
        palindrome_prefix = string[i:]
        if is_palindrome(palindrome_prefix):
            if len(palindrome) < len(palindrome_prefix):
                palindrome = palindrome_prefix

    # Return the palindrome prefix plus reverse of the prefix
    return (palindrome + string[0:len(string) - len(palindrome)])[::-1]

