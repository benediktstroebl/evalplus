def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    # Adjusted slicing to find the longest palindromic suffix
    palindromic_suffix = string[-1:-1*-1]
    # Reverse a string prefix that comes before the palindromic suffix
    reverse_prefix = string[:-1*-1]
    return f"{string}{reverse_prefix}{palindromic_suffix}"