Here's a self-contained Python function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Palindrome finder
    reversed_prefix = string[::-1]
    palindrome = string[:len(reversed_prefix)] + reversed_prefix
    return palindrome
```

This function, `is_palindrome`, checks if a given string is a palindrome, and the `make_palindrome` function uses this check along with a simple algorithm to find the shortest palindrome.