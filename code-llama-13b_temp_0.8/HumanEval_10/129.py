

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
    # Iterate over the string and find the longest palindromic suffix
    for suffix_start_idx in range(len(string)):
        if is_palindrome(string[suffix_start_idx:]):
            suffix_start_idx = suffix_start_idx

    # Find the index of the first non-matching char from the end of the string
    prefix_end_idx = suffix_start_idx
    while prefix_end_idx > 0 and string[prefix_end_idx - 1] != string[suffix_start_idx]:
        prefix_end_idx -= 1

    return string + string[:suffix_start_idx][::-1]

