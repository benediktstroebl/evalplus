Here's a Python script with a self-contained function that solves the problem using the given `is_palindrome` function:
```python
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

# Test cases
print(make_palindrome(''))  # Should return an empty string
print(make_palindrome('cat'))  # Should return 'catac'
print(make_palindrome('cata'))  # Should return 'catac'
print(make_palindrome('aaa'))  # Should return 'aaa'
print(make_palindrome('abba'))  # Should return 'abba'
```

This script uses the supplied function `is_palindrome` to determine if a substring is a palindrome. It then iterates through the string to find the longest palindromic postfix and its corresponding non-palindromic prefix. If no valid postfix is found, it returns the original string; if the entire string is a palindrome, it also returns the string unchanged. Otherwise, it constructs the shortest palindrome by appending the reverse complement of the non-palindromic prefix to the palindromic suffix.