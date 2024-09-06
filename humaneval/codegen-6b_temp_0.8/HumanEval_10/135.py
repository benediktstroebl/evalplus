

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
    longest_palindrome = ''
    len_string = len(string)
    for start in range(len_string):
        for end in range(start, len_string):
            if is_palindrome(string[start:end + 1]):
                if end - start + 1 > len(longest_palindrome):
                    longest_palindrome = string[start:end + 1]
    return longest_palindrome

