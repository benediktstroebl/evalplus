Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    prefix, suffix = palindrome_prefix_suffix(string)
    return prefix + suffix[::-1]

def palindrome_prefix_suffix(string):
    """ Returns the palindrome prefix and suffix of a given string"""
    char = list(string)
    i = 0
    while char[i] == char[i][::-1]:
        i += 1
    left, right = i, len(char) - 1
    return left, right
```

This script provides a solution to the problem of checking if a given string is a palindrome and generating the shortest palindrom that begins with the given string.