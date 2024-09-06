```python
def is_palindrome(string):
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ""
    prefix, postfix = divmod(string, 2)
    return prefix[::-1] + postfix[1:]
```

This code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` generates a palindrome from an input string. The `make_palindrome` function splits the input string into its prefix and postfix and constructs the palindrome by appending the reversed prefix and postfix together.