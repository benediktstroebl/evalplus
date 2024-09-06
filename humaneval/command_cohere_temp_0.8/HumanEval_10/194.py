Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """Returns True if string s is a palindrome, False otherwise."""
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome that starts with string s."""
    if not s:
        return s

    # Find the location of the longest palindromic suffix.
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindromic suffix.
    palindrome_suffix = s[i:]
    s = s[:i]

    # Find the longest palindromic prefix.
    j = 0
    while not is_palindrome(s[:j]+palindrome_suffix):
        j += 1

    return s + palindrome_suffix[::-1][:j]
```