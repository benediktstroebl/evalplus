

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

    # 1. Find the longest postfix of a string that is a palindrome.
    if is_palindrome(string):
        return string

    length = len(string)
    longest_palindromic_postfix = ''
    for i in range(length // 2, 0, -1):
        substring = string[length - i:]
        if is_palindrome(substring):
            longest_palindromic_postfix = substring
            break

    # 2. Append to the end of the string reverse of a prefix that comes before the palindromic suffix.
    prefix_to_add = string[:length - len(longest_palindromic_postfix)]
    return string + prefix_to_add[::-1]

