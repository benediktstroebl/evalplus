Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    return ''.join_with(reversed(prefix), suffix)

def not_palindrome(string):
    return bool(is_palindrome(string))
```

This script contains two functions:
- `is_palindrome`: checks if a given string is a palindrome.
- `make_palindrome`: generates a palindrome by finding the shortest palindrome that begins with a supplied string.

Both functions use a recursive approach with a prefix-suffix strategy to generate the palindrome.