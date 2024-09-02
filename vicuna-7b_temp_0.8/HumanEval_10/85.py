

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
    left, right = 0, len(string) - 1
    while left < right:
        mid = (left + right) // 2
        if string[mid] == string[left]:
            right = mid - 1
        elif string[mid] == string[right]:
            left = mid + 1
        else:
            break
    return string[left:right]

