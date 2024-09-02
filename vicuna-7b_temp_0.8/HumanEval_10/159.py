

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
    if string == '':
        return ''
    palindrome_len = len(string) // 2
    palindrome = string[:palindrome_len]
    prefix = string[:palindrome_len]
    suffix = string[palindrome_len:]
    for suffix_char in suffix:
        if suffix_char not in string:
            break
    prefix_suffix = [prefix[::-1], suffix[::-1]]
    prefix_suffix_len = max(len(prefix_suffix[0]), len(prefix_suffix[1]))
    if suffix_len < prefix_suffix_len:
        prefix_suffix = [prefix[::-1] + suffix[::-1]]
        prefix_suffix_len = len(prefix_suffix[0])
    new_string = prefix + prefix_suffix[0] + suffix[prefix_suffix_len:]
    return new_string

