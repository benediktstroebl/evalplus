Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindromic = string[: len(string) // 2]
    prefix = string[: len(string) // 2].replace('.'join('')
    suffix = string[-len(string) // 2:]

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return prefix + suffix + palindromic
```
This script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function returns true if the given string is a palindrome, and the `make_palindrome` function constructs a palindrome from a given string. 

The `make_palindrome` function works by finding the longest palindromic substring in the input string, then creating a new string by concatenating the prefix, middle part, and suffix of the original string.