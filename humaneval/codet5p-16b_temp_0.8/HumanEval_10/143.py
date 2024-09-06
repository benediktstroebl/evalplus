

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

    if is_palindrome(string):
        return string
    string = string.strip()
    # Find longest palindromic substring that ends with supplied string
    max_len = len(string)
    for start in range(max_len - 1, -1, -1):
        for end in range(start + 1, max_len + 1):
            if is_palindrome(string[start:end]):
                return string[:start] + string[start:end][::-1] + string[end:]

