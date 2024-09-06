def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix of the string.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Extract the palindromic suffix.
    palindromic_suffix = string[i:][::-1]
    original_prefix = string[:i]

    # Extend the string with the reversed prefix and palindromic suffix.
    return make_palindrome(original_prefix) + palindromic_suffix