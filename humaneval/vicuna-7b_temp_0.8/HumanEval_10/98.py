

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
        return string
    string = string[::-1]  # reverse the string
    if string == string[::-1]:
        return string  # if the string is a palindrome, return it
    i = 0
    for j in range(len(string)):
        if string[j] != string[len(string) - j - 1]:
            break
    else:
        return string[::-1]  # if the string is not a palindrome, append reverse of the string prefix that comes before the palindromic suffix
    return string + string[::-1]  # if the string is not a palindrome, append reverse of the string prefix that comes before the palindromic suffix

