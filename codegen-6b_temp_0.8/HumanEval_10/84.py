

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
    longest_palindromic_suffix = None
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            longest_palindromic_suffix = string[i:]
            break
    if longest_palindromic_suffix is None:
        return string

    # We should remove the letter that's in the middle of string
    # Also, do not remove the letter if it's at the beginning of the string
    mid_letter = longest_palindromic_suffix[len(longest_palindromic_suffix) // 2]
    new_string = string[:string.index(mid_letter)] + \
        string[string.index(mid_letter) + 1:][::-1]
    return new_string

