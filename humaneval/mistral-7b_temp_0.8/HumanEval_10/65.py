

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
    # Find the longest suffix that is a palindrome
    def find_longest_suffix_palindrome(string: str) -> str:
        for length in range(1, len(string)):
            if is_palindrome(string[length:]):
                return string[length:]

    # Find the longest prefix that is a palindrome
    def find_longest_prefix_palindrome(string: str) -> str:
        for length in range(1, len(string)):
            if is_palindrome(string[:length]):
                return string[:length]

    # Create a palindrome
    return string[0:len(find_longest_suffix_palindrome(string)) - 1] + find_longest_prefix_palindrome(string)[::-1]

