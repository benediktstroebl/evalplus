

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

    if is_palindrome(string):
        return string

    longest_palindrome = ''
    for i in range(len(string)):
        new_str = string[i:]
        if is_palindrome(new_str):
            longest_palindrome = new_str
            break

    if longest_palindrome == '':
        return string

    result = string + longest_palindrome[::-1]
    return result

