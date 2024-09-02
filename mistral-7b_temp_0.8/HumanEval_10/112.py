

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
    postfix_is_palindrome = False
    if string == '':
        return string
    while True:
        try:
            if is_palindrome(string[1:]):
                postfix_is_palindrome = True
                break
            else:
                string = string[:-1]
        except IndexError:
            # we've already have a palindrome at the beginning of a string
            break
    if not postfix_is_palindrome:
        return ''.join((string, string[::-1]))
    else:
        # reverse prefix that comes before the palindromic suffix
        return ''.join((string, string[:len(string) - len(string[::-1])][::-1]))

