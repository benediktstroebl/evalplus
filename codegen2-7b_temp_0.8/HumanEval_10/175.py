

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
    longest = ""
    for i in range(1, len(string) + 1):
        for p in range(1, len(string) + 1 - i):
            if string[p:(p + i)] == string[(p + i) - 1: -1:-1]:
                longest = string[:p] + string[-1:-1:-1]
                break
    return longest + string[::-1]

