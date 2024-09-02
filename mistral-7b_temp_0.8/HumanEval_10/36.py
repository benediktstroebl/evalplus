

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
    # 1. Get the longest palindromic suffix
    palindrome_len = 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindrome_len = i
    if palindrome_len == 0:
        return string + string[::-1]

    # 2. Get the prefix before palindrome suffix
    prefix_len = 0
    for i in range(len(string) - 1):
        if string[i] == string[palindrome_len]:
            prefix_len = i
            break
    if prefix_len == 0:
        return string + string[palindrome_len:][::-1]

    return string[prefix_len:palindrome_len + 1] + string[::-1][palindrome_len:]

