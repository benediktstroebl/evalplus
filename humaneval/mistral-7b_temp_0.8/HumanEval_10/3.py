

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

    string_length = len(string)

    # find longest palindromic suffix
    suffix_start_index = 0
    while suffix_start_index < string_length:
        suffix = string[suffix_start_index:]
        if is_palindrome(suffix):
            break
        else:
            suffix_start_index += 1

    if suffix_start_index == string_length:
        return string

    # find prefix of string before palindrome suffix
    prefix = string[:suffix_start_index]
    # reverse the prefix
    reversed_prefix = ''.join(reversed(prefix))

    # concatenate reversed prefix and palindromic suffix
    return string[:suffix_start_index] + reversed_prefix + string[suffix_start_index:]

