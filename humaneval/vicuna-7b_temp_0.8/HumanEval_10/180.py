

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
    result = ""
    prefix_len = 0
    suffix_len = 0
    for char in string:
        if char in "aeiouAEIOU":
            prefix_len += 1
        else:
            suffix_len += 1
    prefix = string[:prefix_len]
    suffix = string[-suffix_len:]
    if is_palindrome(prefix) and is_palindrome(suffix):
        result = prefix + suffix
    else:
        for i in range(len(prefix) - suffix_len):
            result += prefix[i]
        for j in range(len(suffix) - prefix_len):
            result += suffix[j]
    return result