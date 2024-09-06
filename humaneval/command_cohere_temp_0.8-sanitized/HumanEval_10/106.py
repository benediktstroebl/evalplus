def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Extract the palindromic suffix
    palindromic_suffix = string[i:]

    # Find the reverse of the prefix up to the palindromic suffix
    prefix = string[:i]
    reverse_prefix = prefix[::-1] if i < len(prefix) else ''

    # Return the shortest palindrome
    return f"{reverse_prefix}{palindromic_suffix}"