

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
    if string == "":
        return ""

    suffix_index = 0
    suffix = string[suffix_index:]
    while suffix_index < len(suffix) and is_palindrome(suffix):
        suffix_index += 1
        suffix = string[suffix_index:]

    prefix = string[:suffix_index]
    prefix_reversed = prefix[::-1]
    return prefix_reversed + suffix + prefix_reversed

