

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
        if not is_palindrome(string[mid:]) and string[mid:mid+1] in string[0:mid]:
            right = mid - 1
        else:
            left = mid + 1
    return string[left:right]

