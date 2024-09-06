

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
    length = len(string)
    palindromic_suffix = ''
    postfix = string[1:]
    while postfix and postfix[-1] == string[-1]:
        postfix = postfix[:-1]
        if len(postfix) > length:
            break
        if is_palindrome(postfix):
            palindromic_suffix = postfix + string[:-1]
            break
    if not palindromic_suffix:
        return string
    else:
        return string[:-len(palindromic_suffix)] + palindromic_suffix[::-1]

