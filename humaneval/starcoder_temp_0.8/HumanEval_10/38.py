

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
    # Find longest palindromic postfix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            break
    # Find reverse palindrome prefix
    for j in range(len(string)):
        if is_palindrome(string[j:len(string)-i+j]):
            break
    # Build the answer
    return string[:i] + string[j:len(string)-i+j][::-1]
