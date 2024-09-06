def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[i:]):
        i -= 1

    # Extract the reverse of the prefix up to the palindromic suffix
    prefix = string[:i]
    reversed_prefix = prefix[::-1]

    # Append the reverse prefix to the string to make a palindrome
    return f'{reversed_prefix}{string[i:]}'