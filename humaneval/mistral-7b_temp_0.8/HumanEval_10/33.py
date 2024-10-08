

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
    string = string.lstrip()
    if is_palindrome(string):
        return string
    max_suffix = ''
    for i in range(1, len(string)):
        if is_palindrome(string[i:]):
            max_suffix = string[i:]
    if max_suffix:
        prefix = string[:max_suffix.find(max_suffix[::-1])+1]
        return prefix+max_suffix[::-1]
    raise ValueError("string not palindrome")
