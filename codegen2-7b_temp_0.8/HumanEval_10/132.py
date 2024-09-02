

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

    if is_palindrome(string):
        return string

    longest_postfix = max(string, key=lambda s: len(s) - len(s.lstrip(string[0])))
    postfix = longest_postfix[::-1]
    if is_palindrome(postfix):
        return postfix + string[:len(postfix)]
    return make_palindrome(postfix + string[:len(postfix)])
