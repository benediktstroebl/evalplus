

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
    if string == '':
        return string

    string_length = len(string)

    ending_index = string_length
    left_index = 0
    right_index = string_length - 1

    while right_index > 0:
        if is_palindrome(string[left_index:ending_index]):
            ending_index -= 1
        else:
            break

    return string[:left_index] + string[ending_index:][::-1] + string[left_index:ending_index]

