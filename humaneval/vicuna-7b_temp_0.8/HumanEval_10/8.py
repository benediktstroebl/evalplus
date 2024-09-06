

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
    length = len(string)
    max_length = length
    palindrome = string
    for i in range(1, length):
        if is_palindrome(palindrome[i:]) and len(palindrome) > i:
            max_length = i
            palindrome = palindrome[:i] + string[i:] + palindrome[i+1:]
    return palindrome[max_length:] if max_length > 0 else ''