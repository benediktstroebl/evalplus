

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
    # Find the longest palindromic suffix
    i = 0
    while i < len(string) // 2 and string[i] == string[-(i+1)]:
        i += 1
    # The palindromic suffix is now at index len(string)-i in the string
    if i == 0:
        # The supplied string is a palindrome
        return string
    else:
        # Reverse the prefix of the string
        prefix = string[:-(i+1)]
        prefix_reversed = prefix[::-1]
        return prefix_reversed + string[-i:]

