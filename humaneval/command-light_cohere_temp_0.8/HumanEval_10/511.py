Here's a self-contained Python function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    else:
        return "".joinindrome(string[::-1]) + string

def not_palindrome(string):
    return "It's a palindrome!" if is_palindrome(string) else "It's not a palindrome!"
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome, and another function `make_palindrome` that uses this helper function to find the shortest palindrome.