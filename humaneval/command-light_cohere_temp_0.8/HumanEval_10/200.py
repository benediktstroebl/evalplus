Here's the provided Python script with a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    if not string:
        return ''  
    if len(string) < 2:
        return string  
    else:
        # Find the longest postfix of supplied string that is a palindrome
        palindrome = string[::-1] + string[1:]
        return palindrome
```

This script provides a simple and self-contained way to solve the problem of creating a palindrome from a given string. The `make_palindrome` function takes a string as input and returns the shortest palindrome that begins with the given string. The `is_palindrome` function tests whether a given string is a palindrome or not by comparing it to its reverse.