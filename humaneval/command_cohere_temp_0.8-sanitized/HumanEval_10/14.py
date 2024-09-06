def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # If no palindromic suffix, return the input
    if i == 0:
        return string

    # Split the string at the palindromic suffix
    prefix, suffix = string[:i], string[-i:]

    # Reverse the prefix and concatenate for a shorter palindrome
    return f"{suffix}{prefix[::-1]}"