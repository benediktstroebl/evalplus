

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
    string = string + str(len(string) - 1) + "c"
    palindromic_prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[:i]):
            palindromic_prefix += string[:i]
    if len(palindromic_prefix) > 1:
        reversed_palindromic_prefix = ''.join(reversed(palindromic_prefix))
        return reversed_palindromic_prefix + string[::-1] + 'c'
    else:
        return palindromic_prefix + string[::-1] + 'c'

