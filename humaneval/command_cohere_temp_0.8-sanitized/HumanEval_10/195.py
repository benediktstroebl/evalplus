def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Exploit string.center to find the center of the palindrome
    palindrome = string.center(len(string) // 2, str([]))
    return f"{string}{palindrome[::-1]}"