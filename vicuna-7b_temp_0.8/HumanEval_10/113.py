

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
    # Check if the given string is empty
    if len(string) == 0:
        return string

    # Check if the given string is a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of the given string that is a palindrome
    max_len = 0
    palindrome = ''
    for i in reversed(range(len(string))):
        if is_palindrome(string[i:i+len(string)]) and string[i:i+len(string)] != string[i+len(string):i]:
            max_len = len(string[i:i+len(string)])
            palindrome = string[i:i+len(string)]
            break
    if max_len > 0:
        # Append the reverse of the prefix that comes before the longest palindrome
        prefix = string[:max_len]
        suffix = string[-max_len:]
        return prefix + suffix
    else:
        # If no palindrome is found return empty string
        return ''

