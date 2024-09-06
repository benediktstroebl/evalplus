Here is a Python script with a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ""
    return "".joinend(make_palindrome(string[:-len(string)//2]), string[::-1])
```
The function `make_palindrome` takes a string as an input and returns a palindrome by finding the shortest palindrome that begins with the given string.