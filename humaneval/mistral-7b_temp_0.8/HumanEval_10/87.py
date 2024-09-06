

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
    start_index = 0
    end_index = len(string)
    while end_index > start_index:
        is_pal = is_palindrome(string[start_index:end_index])
        if is_pal:
            return string[:end_index] + string[::-1][:start_index]
        start_index += 1
        end_index -= 1
    raise ValueError(f'{string} is not a palindrome!')

