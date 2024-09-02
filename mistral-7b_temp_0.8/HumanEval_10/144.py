

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
    string = string.replace(' ', '').lower()
    if not string:
        return ''
    if is_palindrome(string):
        return string
    if len(string) % 2 == 0:
        left_palindrome = string[:len(string) // 2]
        right_palindrome = string[len(string) // 2:]
    else:
        left_palindrome = string[:len(string) // 2 + 1]
        right_palindrome = string[len(string) // 2:]
    if is_palindrome(left_palindrome):
        return left_palindrome + right_palindrome + left_palindrome[::-1]
    return make_palindrome(left_palindrome + right_palindrome)

