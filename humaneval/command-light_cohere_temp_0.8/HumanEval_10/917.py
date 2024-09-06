Here is a self-contained Python script with a function that solves the problem of creating a palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if notstring:
        return ''
    return ''.join(end + ''.reverse(prefix) for end, prefix in zip(reversed(string), string))
```

This script provides a function `is_palindrome` that checks if a given string is a palindrome. It also provides a other function `make_palindrome` that uses a recursive approach to create the shortest palindrome from the given string.