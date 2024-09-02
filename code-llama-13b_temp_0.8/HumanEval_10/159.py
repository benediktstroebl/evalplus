

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

    # If the string is empty, return empty string.
    if not string:
        return ''

    # Iterate over all prefixes in the string and find the longest
    # suffix that is a palindrome.
    longest_palindromic_suffix = ''
    for i in range(len(string)):
        current_suffix = string[i:]
        if is_palindrome(current_suffix) and len(current_suffix) > len(longest_palindromic_suffix):
            longest_palindromic_suffix = current_suffix

    # The prefix before the palindromic suffix is also a prefix of the input string.
    palindromic_prefix = string[:-len(longest_palindromic_suffix)]

    # Append to the end of the string the reverse of the palindromic prefix.
    return string + palindromic_prefix[::-1]

