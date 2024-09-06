Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome that begins with string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:-i]):
        i -= 1

    # Find the longest non-palindromic prefix before that suffix
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    # Return the palindrome concatenated with the non-palindromic prefix
    return make_palindrome(string[:j] + string[i:][::-1]) + string[j:]
```

This code defines two functions:
- The `is_palindrome` function checks whether a given string is a palindrome by comparing it to its reverse.
- The `make_palindrome` function is designed to transform a non-palindromic string into a palindrome by adding the shortest possible prefix. 

Both functions have detailed docstrings that explain their purpose and usage.

These functions allow for precise control over palindrome detection and creation, making them versatile tools for various palindrome-related tasks.