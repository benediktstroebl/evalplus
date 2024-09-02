

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
    # Find the longest postfix that is a palindrome
    n = len(string)
    postfix = string[n-1:]
    postfix_len = len(postfix)
    for i in range(postfix_len):
        if is_palindrome(postfix[i:]) and postfix[i:].strip() != string[i:]:
            prefix = string[:i]
            prefix_len = len(prefix)
            return prefix + postfix[i:]

    # Append the reverse of prefix that comes before the palindromic suffix
    prefix = string[:n-1]
    prefix_len = len(prefix)
    return prefix + postfix[n-1:]

