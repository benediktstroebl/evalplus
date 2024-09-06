def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return string
    
    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1
    
    if i == 0:
        return string
    
    # Reverse the prefix up to the palindromic suffix
    suffix = string[-i:]
    prefix = string[:-i]
    reversed_prefix = prefix[::-1]
    
    # Construct and return the shortest palindrome
    return f"{reversed_prefix}{suffix}"