Here's a Python script with a self-contained function that solves the problem using Markdown code blocks:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string:
    i = len(string) - 1
    while i > 0 and is_palindrome(string[-i:]):
        i -= 1
    # Reverse the prefix up to the palindromic suffix:
    prefix = string[:i]
    return prefix + prefix[::-1]
```

This code defines two functions:
- The `is_palindrome` function checks if a given string is a palindrome by comparing it to its reverse.
- The `make_palindrome` function takes an input string and returns the shortest palindrome that starts with the input. It does this by finding the longest palindromic suffix of the input string and then reversing and concatenating a prefix of the input string that comes before this suffix.