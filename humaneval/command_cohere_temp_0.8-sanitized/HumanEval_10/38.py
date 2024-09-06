from itertools import common_prefix
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(common_prefix(string[::-1], string))
    palindromic_suffix = string[i:]

    # Remove the palindromic suffix from the string
    prefix = string[:-i] if i > 0 else string

    # Reverse the prefix and append to string to create a palindrome
    return f'{palindromic_suffix}{prefix[::-1]}'