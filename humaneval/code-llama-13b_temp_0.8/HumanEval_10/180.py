

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

    # An empty string is a palindrome.
    if string == "":
        return ""

    # Find the longest postfix of a string that is a palindrome.
    longest_palindromic_postfix = ""
    for idx, char in enumerate(string):
        current_substring = string[idx:]
        if is_palindrome(current_substring) and len(current_substring) > len(longest_palindromic_postfix):
            longest_palindromic_postfix = current_substring

    # Now find the shortest palindrome by appending to the end of the string reverse of a prefix that comes before the palindromic suffix.
    prefix = string[0:len(string) - len(longest_palindromic_postfix)]
    return string + prefix[::-1]

