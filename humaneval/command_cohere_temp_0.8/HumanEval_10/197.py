Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix in the input string
    palindrome_suffix = None
    for suffix in range(1, len(string) + 1):
        if is_palindrome(string[-suffix:]):
            palindrome_suffix = suffix
    # If there is no palindrome suffix, return the input string
    if palindrome_suffix is None:
        return string
    # Find the longest non-palindrome prefix of the palindrome suffix
    non_palindrome_prefix = None
    for prefix in range(len(string) - palindrome_suffix + 1):
        if not is_palindrome(string[prefix: -suffix]):
            non_palindrome_prefix = prefix
    # If there is no non-palindrome prefix, return the input string
    if non_palindrome_prefix is None:
        return string
    return make_palindrome(string[non_palindrome_prefix: -palindrome_suffix]) \
           + string[non_palindrome_prefix: ]
```

This code includes both the `is_palindrome` and `make_palindrome` functions based on the provided problem statement and test examples. You can use these functions to test whether a given string is a palindrome and to construct palindromes accordingly. 
```python
# Test if a string is a palindrome
assert is_palindrome("racecar")
assert not is_palindrome("hello")

# Create palindromes
assert make_palindrome("zebra") == "zebrAz"
assert make_palindrome("a") == "a"
assert make_palindrome("cat") == "catac"
``` 
This makes use of the `make_palindrome` function to find the shortest palindrome string that starts with the input string.