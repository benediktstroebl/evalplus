

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
    assert string, "String can't be empty"

    if is_palindrome(string):
        return string

    # find the longest palindromic suffix
    reversed_string = string[::-1]
    suffix_index = 0
    while suffix_index < len(string) and is_palindrome(reversed_string[:suffix_index + 1]):
        suffix_index += 1
    suffix = reversed_string[:suffix_index]

    # find the shortest palindromic prefix that comes before the palindromic suffix
    prefix_index = 0
    while prefix_index < suffix_index and not is_palindrome(reversed_string[prefix_index:suffix_index]):
        prefix_index += 1
    prefix = reversed_string[prefix_index:suffix_index]

    return string + prefix[::-1]

