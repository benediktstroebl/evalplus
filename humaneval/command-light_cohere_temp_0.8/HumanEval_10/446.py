```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join(c if c.is_palindrome(c) else c for c in string)
    else:
        return string
```

This script defines a function `make_palindrome` that creates the shortest palindrome for a given string. The `is_palindrome` function checks if a string is already a palindrome.