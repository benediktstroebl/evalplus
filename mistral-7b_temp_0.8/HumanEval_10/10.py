

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

    # Find the longest postfix of supplied string that is a palindrome.
    # Length of the substring will be 1 by default, and we'll check for longer
    # palindromes by appending a single character to the end of the string.
    palindrome = string[-1]

    # Since the string is being iterated from the end to the beginning, we have to iterate the reversed string.
    for i in range(len(string) - 1, 0, -1):
        if is_palindrome(string[i:]):
            palindrome = string[i:]
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return string + palindrome[::-1]

