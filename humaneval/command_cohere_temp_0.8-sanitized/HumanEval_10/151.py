def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    # Convert to lowercase to handle cases like "Aba" -> "aBa"
    string = string.lower()
    
    if not string:
        return string
    
    # Find the longest palindromic postfix and corresponding prefix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1
    
    if i == 0:
        return string
    
    j = 0
    while j < i and not is_palindrome(string[:j]+string[-i:]):
        j += 1
    
    if j == i:
        return string
    
    return string[:j] + string[i-j:i] + string[j:][::-1]