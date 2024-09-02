

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
    shortest_palindrome = max([len(postfix) for prefix in string for postfix in repeat(str(prefix), len(prefix))], key=len)
    return ''.join([''.join(str(prefix).split(''))[-shortest_palindrome] + ''.join([''.join(str(prefix)[-1]) for prefix in string if is_palindrome(prefix)])])

