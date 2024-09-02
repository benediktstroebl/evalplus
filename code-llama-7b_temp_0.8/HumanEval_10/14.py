

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
    # Find the longest palindromic prefix in the string
    prefix_index = 0
    while prefix_index < len(string) - 1:
        if is_palindrome(string[prefix_index:]):
            break
        prefix_index += 1
    # Find the longest palindromic suffix in the string
    suffix_index = len(string) - 1
    while suffix_index > prefix_index:
        if is_palindrome(string[:suffix_index]):
            break
        suffix_index -= 1
    # Build palindrome
    return string[:suffix_index] + string[prefix_index:suffix_index][::-1] + string[suffix_index:]

