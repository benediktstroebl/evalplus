

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
    if not string:
        return ''
    n = len(string)
    longest_palindromic_suffix_start = 0
    for i in range(n):
        palindrome_len = 0
        for j in range(i, n):
            if is_palindrome(string[i:j + 1]):
                palindrome_len = j - i + 1
                longest_palindromic_suffix_start = i
        if palindrome_len == n:
            break

    prefix_len = longest_palindromic_suffix_start
    return string[:prefix_len] + string[::-1]

