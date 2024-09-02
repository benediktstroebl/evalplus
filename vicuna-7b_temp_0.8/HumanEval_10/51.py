

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
    # Find the longest postfix of the string that is a palindrome
    palindrome_len = len(string)
    max_palindrome_len = 0
    for i in range(1, palindrome_len):
        if is_palindrome(string[i:i + 2]) and (i + 2) <= palindrome_len:
            max_palindrome_len = i + 2
    max_palindrome = string[palindrome_len - max_palindrome_len:palindrome_len]

    # Append the reverse of the string prefix that comes before the palindromic suffix
    prefix_len = len(string)
    prefix = string[:prefix_len - max_palindrome_len]
    reverse_prefix = string[::-1][:prefix_len - max_palindrome_len]
    return prefix + max_palindrome + reverse_prefix

