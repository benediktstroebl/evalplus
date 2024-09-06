Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """Returns True if string s is a palindrome, False otherwise."""
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome that begins with the supplied string."""
    if not string:
        return string

    # Find the location of the longest palindromic suffix
    left = 0
    right = len(string) - 1
    max_len = 1
    while left < right:
        if is_palindrome(string[left:right + 1]):
            max_len = max(max_len, len(string[left:right + 1]))
        else:
            left += 1
        right -= 1

    # Reverse the non-palindromic prefix up to the length of the palindromic suffix and append
    result = string[right:right + max_len] + string[0:left][::-1]
    return result
```