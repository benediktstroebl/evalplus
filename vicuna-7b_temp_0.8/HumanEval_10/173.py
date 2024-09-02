

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
    if string == '':
        return ''
    else:
        prefix = string[:len(string) // 2]
        suffix = string[len(string) // 2:]
        if is_palindrome(suffix):
            if len(prefix) > len(suffix):
                suffix = suffix[::-1] + suffix
                return prefix + suffix
            else:
                return prefix + suffix
        else:
            return make_palindrome(suffix) + make_palindrome(prefix[::-1])

