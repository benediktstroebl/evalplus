

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
    string_length = len(string)
    max_length = string_length
    start_index = 0
    while True:
        end_index = string.find(string[start_index:], is_palindrome)
        if end_index == -1:
            break
        end_index += len(string[start_index:])
        max_length = max(max_length, end_index)
        start_index += end_index
    return string[start_index:end_index] + string[0:start_index]

