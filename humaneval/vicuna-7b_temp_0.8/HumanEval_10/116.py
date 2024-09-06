

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
    if not string:
        return string
    if len(string) == 1:
        return string
    elif string[0] in string[1:]:
        return re.sub(string[1:], string[::-1], string)
    else:
        prefix = string.split("")[-1].split(".")[0]
        suffix = string.split("")[0].split(".")[0]
        return prefix + re.sub(suffix, string[::-1], string)

