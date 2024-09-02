

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

    s = string.strip()
    if s == "":
        return s

    if is_palindrome(s):
        return s + s

    last_palindromic_suffix = s
    for i in range(len(s)):
        last_palindromic_suffix = s[i:]
        if is_palindrome(last_palindromic_suffix):
            break

    prefix = s[:i]
    return prefix + last_palindromic_suffix[::-1]
