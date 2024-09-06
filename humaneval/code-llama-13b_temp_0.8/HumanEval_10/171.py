

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

    # this check is important to avoid index error when the for loop start below
    if not string:
        return string

    # find the longest postfix that is a palindrome
    for index in range(len(string)):
        if is_palindrome(string[-1 * (index + 1):]):
            break

    # at this point we have the longest palindrome postfix at the end of the string
    # we need to find the prefix that comes before it, and reverse it
    prefix_end_index = len(string) - 1 - index
    prefix_to_add = string[:prefix_end_index][::-1]

    # now we can add prefix to the end of string, and we have a shortest palindrome that begins with the string
    return string + prefix_to_add

