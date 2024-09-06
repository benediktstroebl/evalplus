

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

    for i, char in enumerate(string):
        if is_palindrome(string[i:]):
            return string[:i] + string[i:][::-1]

    return string
    # Postfix of supplied string that is a palindrome:
    # string[::-1]
    # - [::-1] is slicing reverse of string
    # - string[:i] is slicing from beginning to i-1th char
    # - string[i:] is slicing from i to the end of string
    # string[:i] + string[i:][::-1] is concatenation of reversing string prefix to the end of string
    # if string == string[::-1]:
    #   return string
    # else:
    #   return make_palindrome(string)

