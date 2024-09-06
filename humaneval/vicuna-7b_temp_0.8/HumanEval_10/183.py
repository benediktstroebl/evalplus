

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
    # check if the string is empty
    if string == '':
        return ''

    # get the length of the string
    length = len(string)

    # check for palindrome
    if is_palindrome(string):
        # return the original string as a palindrome
        return string

    # find the longest postfix that is a palindrome
    start = 0
    end = len(string) - 1
    while start <= end:
        middle = (start + end) // 2
        if is_palindrome(string[middle:middle + 1]) and is_palindrome(string[middle + 1:middle + 2]):
            start = middle + 2
        else:
            end = middle - 1
    postfix = string[start:end + 1]

    # append the reverse of the string prefix that comes before the palindromic suffix
    prefix = string[:start]
    return prefix + string[end + 1:].reverse() + postfix

