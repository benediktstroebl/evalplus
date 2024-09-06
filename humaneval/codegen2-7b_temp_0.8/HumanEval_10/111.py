

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
    index = 0
    while True:
        found = False
        for i in range(index, len(string)):
            if is_palindrome(string[i:]) and not found:
                found = True
                suffix = string[index:i]
                reverse = suffix[::-1]
                string += reverse
                index = i + len(reverse)
                break
        if not found:
            break
    return
