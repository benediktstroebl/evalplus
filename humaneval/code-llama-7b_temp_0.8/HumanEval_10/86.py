

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
    # Find the longest postfix of supplied string that is a palindrome.
    end_index = 0
    while end_index < len(string):
        if is_palindrome(string[0:end_index + 1]):
            break
        end_index += 1
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    prefix = string[0:end_index]
    suffix = string[end_index:][::-1]
    return prefix + suffix

