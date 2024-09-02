

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
    # Find the longest postfix of supplied string that is a palindrome
    suffix_length = len(string)
    suffix = string[suffix_length-1:suffix_length-1]
    while suffix == suffix[::-1]:
        suffix = suffix[0]
        suffix_length -= 1
    suffix_index = len(suffix) - 1
    longest_palindrome = suffix[:suffix_index]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    reverse_suffix = string[:suffix_index]
    new_string = string[:suffix_length] + string[suffix_length-1:] + reverse_suffix
    return new_string

