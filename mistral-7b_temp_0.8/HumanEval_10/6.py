

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
    string = string.strip()
    # make sure we are dealing with a non-empty string
    if not string:
        return ''

    # initialize the result string
    result = ''

    # find the length of the longest palindromic suffix of the string
    start = 0
    end = len(string)
    while end > 0 and is_palindrome(string[start:end]):
        start += 1
        end -= 1

    # append to the result the prefix of the string before the palindromic suffix
    result += string[:start]
    # reverse the result and append to it the palindromic suffix
    result += string[start:end][::-1]
    return result

