

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

    # reverse the input string
    rev_input = string[::-1]
    # we start from the beginning of the input string and try to find the first index where given string is palindrome
    for index in range(len(string)):
        # if the reversed input string is a palindrome then it means we can append to the end of the input string
        # reverse of a string prefix that comes before the palindromic suffix.
        if rev_input[:len(string) - index] == string[:len(string) - index]:
            return string + string[:index][::-1]

    return string

