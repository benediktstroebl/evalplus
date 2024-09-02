

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
    # Find longest suffix ending with a palindromic substring
    max_suffix_length = 0
    max_suffix_end = 0
    for i in range(len(string)):
        for j in range(len(string) - i):
            if is_palindrome(string[i:len(string) - j]):
                max_suffix_length = len(string) - i - j
                max_suffix_end = len(string) - j
                break
        if max_suffix_length > 0:
            break
    # Reverse the suffix
    suffix = string[max_suffix_end:]
    suffix = suffix[::-1]
    # Append suffix to front of supplied string
    result = string[0:max_suffix_end] + suffix
    return result

