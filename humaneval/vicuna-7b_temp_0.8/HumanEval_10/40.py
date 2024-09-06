

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
    n = 1
    start = string
    while True:
        for i in range(1, len(start)):
            if start[i:i+2] == start[::-1][:i-1] and is_palindrome(start[i:i+2]):
                start = start[i+1:] + start[i:i+2]
                n += 1
                break
        else:
            start = string[::-1][:len(string)-1] + start[1:]
            break
    return start

