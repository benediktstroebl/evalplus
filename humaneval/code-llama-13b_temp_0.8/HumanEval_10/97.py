

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
        return string
    # find longest postfix that is a palindrome and remember its length
    longest_palindromic_postfix_length = 0
    for idx in reversed(range(len(string))):
        current_suffix = string[idx:]
        if is_palindrome(current_suffix):
            longest_palindromic_postfix_length = len(current_suffix)
        else:
            break
    # now build the palindrome by adding to the end the reverse of
    # a string prefix that comes before the palindromic suffix
    return string + string[:longest_palindromic_postfix_length][::-1]

