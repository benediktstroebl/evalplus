

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
    string = string.strip()
    if not string:
        return ''
    left = len(string) - 1
    right = len(string)
    while left >= 0 and right < len(string):
        if not is_palindrome(string[left:right]):
            left -= 1
            right += 1
        else:
            break

    prefix = string[:left + 1]
    suffix = string[right:]
    return prefix + suffix[::-1]

