

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
    m = len(string) // 2
    start_idx = 0
    end_idx = m
    while start_idx <= end_idx:
        if is_palindrome(string[start_idx:end_idx]) and string[start_idx:end_idx] != string[start_idx:end_idx][::-1]:
            return string[start_idx:end_idx]
        start_idx += 1
        end_idx = start_idx - 1
    return string

