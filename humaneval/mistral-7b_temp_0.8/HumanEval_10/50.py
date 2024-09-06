

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

    # Create a list of all substrings of given string
    substrings = [string[i:] for i in range(len(string))]

    # Find the longest palindromic suffix
    max_length = 0
    max_substrings = []
    for substring in substrings:
        if is_palindrome(substring):
            max_length = len(substring)
            max_substrings.append(substring)
    max_substring = max_substrings[0]

    # Find a prefix that matches the reverse of the palindromic suffix
    for i in range(len(string) - 1, -1, -1):
        prefix = string[:i]
        if prefix == max_substring[::-1]:
            break

    return prefix + max_substring + prefix[::-1]

