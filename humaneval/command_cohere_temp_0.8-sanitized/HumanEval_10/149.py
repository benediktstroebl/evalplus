def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return string
    
    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:-i-1]):
        i -= 1
    
    # Reverse the prefix up to the palindromic suffix
    prefix = string[:i]
    reversed_prefix = prefix[::-1]
    
    # Append the reversed prefix to the string to make a palindrome
    result = string[:i] + reversed_prefix
    return result