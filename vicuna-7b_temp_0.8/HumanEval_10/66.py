

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
    prefix_len = 0
    suffix_len = 0
    suffix = ''
    for i in range(1, len(string)):
        if is_palindrome(string[i:]) and string[i:i+1] != string[i:i+1][::-1]:
            suffix_len = 1
            suffix = string[i:i+1]
        elif is_palindrome(string[i:i+1]):
            suffix_len += 1
            suffix = string[i:i+1]
            prefix = string[prefix_len:prefix_len+len(suffix)]
            prefix_len += len(suffix)
    return prefix + suffix[::-1]

