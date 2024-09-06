

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
    string = string.lower()
    if string == '':
        return ''

    suffix_length = 1
    while suffix_length <= len(string):
        suffix = string[len(string) - suffix_length :]
        if is_palindrome(suffix):
            prefix = string[:len(suffix)]
            if is_palindrome(prefix[::-1]):
                return prefix[::-1] + suffix + prefix[::-1]
            break
        suffix_length += 1

    return ''
