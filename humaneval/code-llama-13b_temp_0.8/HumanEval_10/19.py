

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
    # Step 1: find the longest suffix that is a palindrome.
    for i in range(len(string) // 2, -1, -1):
        if is_palindrome(string[i:]):
            break
    # Step 2: append to the end of string reverse of the prefix.
    return string + string[:i][::-1]

