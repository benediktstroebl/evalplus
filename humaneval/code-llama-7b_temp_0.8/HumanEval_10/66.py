

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
    # Boundary condition
    if is_palindrome(string):
        return string

    # Find the index of first character in the string that is not a palindrome.
    # Note, this is exactly the same as the first character that can not be included in the palindrome prefix.
    start_index = 0
    while start_index < len(string) and is_palindrome(string[start_index:]):
        start_index += 1

    if start_index == len(string):
        return string

    # We found the longest palindrome suffix of the string. Now we need to find the palindrome prefix that starts right
    # before it.
    prefix = ''
    end_index = len(string) - 1
    while end_index >= 0 and start_index <= len(string) - 1:
        if string[end_index] == string[start_index]:
            prefix = string[end_index] + prefix
            end_index -= 1
            start_index += 1
        else:
            break

    return string + prefix
