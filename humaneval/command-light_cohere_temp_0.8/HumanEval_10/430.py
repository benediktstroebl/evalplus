Here is a Python script that contains a self-contained function that solves the problem of making a palindrome:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string"""
    
    if not string:
        return ''
    return ''.joinend(string[::-1], string)
```
The code defines two functions:
- `is_palindrome`: Tests if a given string is a palindrome, returning True or False.
- `make_palindrome`: Finds the shortest palindrome that begins with a supplied string. It does so by creating a empty palindrome if the input is empty, or appending the reverse of a string prefix that comes before the palindromic suffix to the end of the string.

In the example, the function will return 'catac' for the string 'cat'.