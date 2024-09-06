

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
    # Check if the string is already a palindrome.
    if is_palindrome(string):
        return string
    # Take the last character.
    last_char = string[-1]
    # Check if the last character is a palindrome.
    if is_palindrome(string[:-1]):
        return string[:-1] + last_char + string[:-1][::-1]
    # Otherwise, take the next character.
    next_char = string[-2]
    # Check if the last two characters are a palindrome.
    if is_palindrome(string[:-2]):
        return string[:-2] + last_char + string[:-2][::-1] + next_char
    # Otherwise, repeat with the next character.
    return make_palindrome(string[:-2]) + last_char + string[:-2][::-1] + next_char

