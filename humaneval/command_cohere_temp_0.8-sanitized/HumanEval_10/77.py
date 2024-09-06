def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[-i-1:]):
        i -= 1

    # Extract the palindromic suffix
    palindrome_suffix = string[-i-1:][::-1]
    new_string = string[:-i-1] if i != len(string) - 1 else string

    # Append the reverse of the prefix to make a palindrome
    new_string += palindrome_suffix[::-1]

    return new_string