

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

    # find longest suffix that is a palindrome
    i = 0
    while i < len(string) / 2:
        if string[i]!= string[-1 - i]:
            break
        i += 1
    # in case if there is no such palindrome
    if i == 0:
        return string + string[::-1]
    # extract prefix and suffix
    prefix = string[0:i]
    suffix = string[-1 - i:]
    # remove suffix from original string and reverse it
    result = string[:-1 * i]
    result += suffix[::-1]
    # add prefix and suffix to the result
    result += prefix
    return result

