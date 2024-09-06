Here is a self-contained Python function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    elif len(string) == 1:
        return string
    
    palindrome = string[:] + string[-1:]
    return palindrome
```
The `is_palindrome` function checks if the input string is a palindrome, and the `make_palindrome` function returns the shortest palindrome that begins with the supplied string.