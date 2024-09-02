

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
    # 1. Find the longest palindromic suffix
    suffix = find_longest_palindromic_suffix(string)
    if is_palindrome(suffix):
        return string + suffix[::-1]

    # 2. Reverse the prefix of the string and find palindromic suffix again.
    prefix = string[:-len(suffix)]
    prefix_suffix = find_longest_palindromic_suffix(prefix[::-1])

    # 3. Palindromic suffix found.
    if is_palindrome(prefix_suffix):
        return prefix[::-1] + prefix_suffix + suffix[::-1]

    # 4. Palindromic suffix not found.
    return string + suffix[::-1]

