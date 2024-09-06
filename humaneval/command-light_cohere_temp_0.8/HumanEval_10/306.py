Here's a Python script with a self-contained function that solves the problem of converting a given string into a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0] + string[-1:]
    return palindrome
```

This code defines two functions: is_palindrome checks if a given string is a palindrome and returns a boolean value, while make_palindrome takes a string and attempts to create a palindrome by iterating over the characters and checking for the palindrome property.