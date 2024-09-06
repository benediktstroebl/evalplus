Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome, false otherwise."""
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s."""
    if not s:
        return s

    # Find the longest palindromic suffix.
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(s[j:i+1]):
        j += 1

    # Reverse the non-palindromic prefix and concatenate.
    return make_palindrome(s[j:i+1][::-1]) + s[:j]

# Test cases:
print(make_palindrome('cat'))  # Expected output: 'catac'
print(make_palindrome('cata'))  # Expected output: 'catac'
print(make_palindrome('a'))  # Expected output: 'aa'
print(make_palindrome('ab'))  # Expected output: 'abba'
```

This script includes the `is_palindrome` function, which is an essential part of the `make_palindrome` algorithm. The `make_palindrome` function uses the former to find the locations of the palindromic prefix and non-palindromic suffix in the input string s. It then reverses the non-palindromic prefix and concatenates it with the palindromic prefix to create the shortest palindrome possible that starts with the input string.