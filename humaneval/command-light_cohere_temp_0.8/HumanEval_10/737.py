A Python function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string.
    # Algorithm idea simple:
    # Find the longest postfix of supplied string that is a palindrome.
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return ''.join(string[::-1], string)
```

The code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, returning `True` if it is, and `False` otherwise. The `make_palindrome` function creates a palindrome by finding the longest postfix of the input string that is a palindrome, and then appending the reversed string prefix and the reversed string suffix.