

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
    if len(string) == 0:
        return string
    string = string + 'a'  # Add a character so we can reverse the string
    string_reversed = string[::-1]
    suffix = ''
    prefix = string[:-1]
    longest_palindrome = 0
    for i in range(len(string_reversed) - 1):
        if string_reversed[i] == prefix[i] and is_palindrome(prefix[i]):
            suffix += string_reversed[i]
            longest_palindrome = max(longest_palindrome, i + 1)
        else:
            suffix += string_reversed[i]
    return prefix[:longest_palindrome] + suffix[::-1]