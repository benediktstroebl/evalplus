

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
    last_palindromic_index = 0
    max_palindromic_prefix_length = 0
    for i in range(1, len(string)):
        if is_palindrome(string[last_palindromic_index:i]):
            max_palindromic_prefix_length = i - last_palindromic_index
        last_palindromic_index = i

    return string[last_palindromic_index:last_palindromic_index + max_palindromic_prefix_length] + string[::-1][:last_palindromic_index + max_palindromic_prefix_length]

