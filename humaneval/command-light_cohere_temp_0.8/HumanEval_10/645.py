Here is a self-contained Python function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))
```

This code defines a function `is_palindrome` that checks if a given string is a palindrome, and a function `make_palindrome` that finds the shortest palindrome that begins with a supplied string. The function `not_palindrome` checks if the input is not a palindrome and returns the original string.  The palindrome for the input ''.