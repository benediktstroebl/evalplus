

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
    string = string.lower()
    max_length = len(string)
    if not string:
        return string
    # Find a palindromic suffix
    left_end = 0
    right_end = len(string) - 1
    while right_end > left_end:
        if string[left_end] != string[right_end]:
            break
        left_end += 1
        right_end -= 1
    if right_end == left_end:
        return string + string[::-1]
    else:
        # Split string into prefix and suffix
        prefix = string[:left_end]
        suffix = string[right_end:]
        # Find a palindromic prefix
        for i in range(left_end, len(string) - 1, -1):
            if is_palindrome(prefix + suffix[i:]):
                return prefix + suffix[:i] + suffix[i:][::-1]

