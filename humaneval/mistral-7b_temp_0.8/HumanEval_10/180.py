

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
    string_len = len(string)
    if string_len == 0:
        return ''

    string_prefix = string[:string_len // 2]
    string_suffix = string[string_len // 2:]

    if is_palindrome(string_prefix):
        string_prefix_len = string_len // 2
    else:
        string_prefix_len = string_len // 2 - 1

    string_prefix_len += 1
    string_prefix_len_1 = string_prefix_len - 1

    # Check if string is a palindrome
    if string_prefix_len == string_prefix_len_1:
        return string

    # Find a palindrome suffix
    for i in range(1, string_prefix_len):
        if is_palindrome(string_suffix[:i]):
            palindrome_suffix_len = i
            break

    # Append reverse string prefix to the end of a string
    string_palindrome_prefix = string[:string_prefix_len]
