

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
    length = len(string)
    # find the longest palindrome in the string
    for i in range(length, 0, -1):
        if is_palindrome(string[:i]):
            break

    if i == length:
        return string + string[::-1]
    else:
        # find the shortest postfix that is palindrome
        for j in range(length, i, -1):
            if is_palindrome(string[i:j]):
                break
        return string[:i] + string[i:j][::-1] + string[j:]

