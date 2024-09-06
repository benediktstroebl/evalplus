

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
        return ''

    # Find longest palindrome suffix
    end = len(string)
    while end > 0:
        if is_palindrome(string[:end]):
            break
        end -= 1

    # If there was no palindrome suffix, append it to the beginning.
    if end == 0:
        return string + string[::-1]

    # Find the shortest prefix
    start = 0
    while start < len(string) - end:
        if is_palindrome(string[start: end + start]):
            break
        start += 1

    # We have prefix and suffix. Append prefix to the end and remove it from the beginning of the string.
    return string[start: end + start] + string[:start] + string[end + start:]
