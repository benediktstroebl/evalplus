

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
    # find the longest postfix of supplied string that is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            longest_palindromic_postfix = string[:i]
            break
    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    palindromic_prefix_with_reverse = longest_palindromic_postfix[::-1]
    return string + palindromic_prefix_with_reverse
