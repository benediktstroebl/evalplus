

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
    palindrome, suffix = '', string
    for i in range(1, len(palindrome)):
        if palindrome[i:i+2] != palindrome[i+2:i+2+len(palindrome[:i+2])]:
            break
        suffix = palindrome[i:i+2]
        palindrome = palindrome[:i] + reverse(suffix) + palindrome[i+2:]
    return palindrome
