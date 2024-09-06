Here's the Python script with a self-contained function that solves the problem of creating a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        return ''.join_split(string)[::-1] + make_palindrome(string[::-1])

def not_palindrome(string):
    return is_palindrome(make_palindrome(string))
```
The function `make_palindrome` returns the shortest palindrome that begins with the string.

The function `is_palindrome` checks if the string is a palindrome, and returns `True` if it is a palindrome and `False` otherwise.