Here is a Python script with a self-contained function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return ''.join
```

This script provides a test function that checks whether a given string is a palindrome. The `make_palindrome` function uses the `is_palindrome` to see if the string is already a palindrome, and if it is not, it appends the string reversed to itself to create a palindrome.